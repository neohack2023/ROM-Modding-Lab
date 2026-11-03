# SMB3 Three Shields: lossless derived-ROM vault

This tooling keeps historical **derived** Super Mario Bros. 3 NES builds reproducible without storing repeated full ROM binaries in source control. It requires user-supplied, verified pristine ROM files. **No game ROM files are included here.**

## Scope

The Host 02 NES workspace has seven historical `build/working/*.nes` revisions. All seven have been represented by compressed IPS deltas (zlib) with a SHA-256 manifest. Each can reconstruct byte-for-byte from the user's **USA PRG1 / Rev 1** original. The separate **USA PRG0 / Rev 0** pristine ROM and the published PRG0/PRG1 IPS files are protected and excluded from retirement.

The portable utility [`tools/smb3_rom_delta_vault.py`](../tools/smb3_rom_delta_vault.py) is environment-configured, does not contain private machine paths, and has **no deletion command**.

## Commands (PowerShell)

Set the three inputs for your own machine:

```powershell
$env:SMB3_WORKSPACE_ROOT = 'path\to\SMB3_HEALTH_BAR_NES_01'
$env:SMB3_PRG1_SOURCE = 'path\to\original_PRG1.nes'
$env:SMB3_PRG0_SOURCE = 'path\to\original_PRG0.nes'
python tools/smb3_rom_delta_vault.py verify
python tools/smb3_rom_delta_vault.py status
python tools/smb3_rom_delta_vault.py restore SMB3_NES_SHIELD_ALPHA.nes
```

For initial setup, `build` creates `vault/derived_roms/manifest.json` and compressed deltas from seven **existing working ROMs**, but refuses to replace an existing vault manifest. `verify` validates the ROM source, compressed-delta SHA, underlying IPS SHA, reconstructed ROM SHA and existing file parity if present. `restore` will only create a missing, whitelisted target in `build/working`, with strict hash checks and an atomic rename. It will not overwrite a drifting existing file.

## Protected SHA-256 originals

| ROM | Expected original SHA-256 |
| --- | --- |
| USA PRG0 / Rev 0 | `6ea0777ca520ba7ad7b0ea0f6452140d59aa0b1dffe5045cb1e8020dde10c267` |
| USA PRG1 / Rev 1 | `4377a7f5e6eb50bdd2ac6f249bf1a7085500aca8eb41f38545c3a2731c51a579` |

## Host 02 acceptance (2026-11-02)

- Seven compressed historical deltas created, **34,623 bytes** total versus 2,752,624 bytes for the seven full-size files.
- All seven reconstructed byte-for-byte using the expected original PRG1, checked by SHA-256.
- Legacy Playtest 01 and Playtest 02 builder scripts now restore their working inputs on demand and preserve source-script rollback snapshots.
- Revision-specific Mesen tests after builder migration: **14/14** seeded-suit collision cases and **6/6** invulnerability/normal-damage cases passed.
- External consumer scan: 434 bounded text/config files, zero exact-name references; 46 oversized files excluded. Not proof of zero unknown consumers.
- Exactly **three** previously unreferenced historical working builds were retired after independent IPS reconstruction, a successful real restore test for each, and unchanged protected-source/patch hashes. **1,179,696 bytes** reclaimed.
- Four other working binaries and all live PRG0/PRG1/GOLD builds remain on Host 02 because their use is not yet eliminated.
- Public ROM patch releases, original source ROM files, and published QA files were not deleted, replaced or repackaged.

The private Host 02 workspace contains machine-local receipts, the entire SHA manifest, and the protected IPS inventory. Keep those private. This public repository deliberately publishes only the utility, instructions and patch releases, not user-owned original ROM binaries or machine-local paths.

## Rollback and further retirement

Recreate a previously retired working build with the `restore` command above (or the Host 02 `scripts/rom_delta_vault.py` equivalent). Compare its SHA-256 with the vault manifest before using it.

**Do not retire more builds** without repeatable dependency analysis, exact reconstruction, both ROM revisions' regression checks, current emulator process inspection, and a rollback receipt. The existing full gameplay checklist for pipes, naturally obtained suits, and two-player behavior remains open.
