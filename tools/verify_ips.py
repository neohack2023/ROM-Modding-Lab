#!/usr/bin/env python3
"""Verify a ROM patch against a declared original and expected output.

Usage:
  python tools/verify_ips.py SOURCE.nes PATCH.ips --source-sha256 HEX --patch-sha256 HEX --output-sha256 HEX
Read-only: does not write a patched ROM.
"""
import argparse
import hashlib
from pathlib import Path

def sha(data):
    return hashlib.sha256(data).hexdigest()

def apply_ips(source, patch):
    if not patch.startswith(b"PATCH"):
        raise ValueError("Invalid IPS header")
    output = bytearray(source)
    i = 5
    while True:
        if i + 3 > len(patch):
            raise ValueError("Truncated IPS")
        addr = patch[i:i+3]
        i += 3
        if addr == b"EOF":
            break
        offset = int.from_bytes(addr, "big")
        if i + 2 > len(patch):
            raise ValueError("Missing record length")
        count = int.from_bytes(patch[i:i+2], "big")
        i += 2
        if count:
            if i + count > len(patch):
                raise ValueError("Truncated record data")
            data = patch[i:i+count]
            i += count
        else:
            if i + 3 > len(patch):
                raise ValueError("Truncated RLE record")
            size = int.from_bytes(patch[i:i+2], "big")
            data = patch[i+2:i+3] * size
            i += 3
        end = offset + len(data)
        if end > len(output):
            output.extend(b"\x00" * (end-len(output)))
        output[offset:end] = data
    if len(patch) - i == 3:
        size = int.from_bytes(patch[i:i+3], "big")
        del output[size:]
        if len(output) < size:
            output.extend(b"\x00" * (size-len(output)))
    elif len(patch) != i:
        raise ValueError("Unexpected bytes following IPS EOF")
    return bytes(output)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("source", type=Path)
    p.add_argument("patch", type=Path)
    p.add_argument("--source-sha256", required=True)
    p.add_argument("--patch-sha256", required=True)
    p.add_argument("--output-sha256", required=True)
    args = p.parse_args()
    original = args.source.read_bytes()
    patch = args.patch.read_bytes()
    for label, actual, expected in (
        ("source", sha(original), args.source_sha256),
        ("IPS patch", sha(patch), args.patch_sha256),
        ("patched output", sha(apply_ips(original, patch)), args.output_sha256),
    ):
        if actual.lower() != expected.lower():
            raise SystemExit(f"FAIL {label}: {actual} != {expected}")
        print(f"PASS {label}: {actual}")
    print("Verified. No ROM output written.")

if __name__ == "__main__":
    main()
