# Automated Three Shields P0 probes

These scripts and evidence cover **USA PRG0** and **USA PRG1**, using distinct
native Mesen checkpoints for each ROM revision. See [full community checklist](../REGRESSION_TESTING.md).

## Verified probes (Mesen 2.2.1)
- **14 suit-state cases:** Small, Big, Fire, Raccoon, Frog, Tanooki and Hammer on each ROM.
  A controlled suit-byte seed is followed by a natural moving-enemy collision.
  Every case yielded one shield lost, original suit downgrade, and no life lost.
- **6 protection cases:** For each ROM: no protection, flashing invulnerability,
  and Star invincibility. Baselines take one shield; both guards preserve three.
- [Machine-readable results](p0_regression_results.json).

## Still open
- Native acquisition of each power-up and its complete visual / ability state.
- Pipe and bonus-room entry/exit with HP persistence.
- Luigi/two-player and multiworld/long-play regression.

## Running the Lua fixtures

These are **Mesen Lua fixtures**, not regular Lua or ROM patches. A Mesen
test-runner session must supply the appropriate environment variables:

- `NES_TEST_FIXTURE`: path to a Mesen save state created by the **same revision**.
- `NES_TEST_OUT`: existing output directory (raw events and screenshots).
- `NES_TEST_SUIT`: integer from 0 to 6 for `p0_suit_probe.lua`.
- `NES_GUARD_MODE`: `none`, `flash`, or `star` for `p0_guard_probe.lua`.

The run must restore a bank-qualified, revision-matching gameplay checkpoint.
The scripts write only test RAM and evidence files. They do not modify input ROMs.
The recorded run used Host 02 wrappers under the private AIOS NES workspace
(`scripts/run_p0_suit_matrix.py`, `scripts/run_p0_guards.py`).
Those wrappers use absolute Host 02 paths and are not portable by themselves.

**Do not check off community suit/pipe tests just because these probes passed.**

## Pipe-transition investigation (not passed)

The [passive pipe recorder](p0_pipe_tracker.lua) watches `Level_PipeMove` ($0571), `Player_InPipe` ($058C), `Level_JctCtl` ($03DE), scene, and HP. It never writes pipe-control RAM.

A bounded auto-run reached a pit and died on both revisions. Although $058C briefly became nonzero, the native pipe-movement and junction controls stayed at zero. See the [qualification record](p0_pipe_qualification.json). **No pipe traversal has passed.** The next gate needs a genuine in-level entry, destination, and unchanged HP.
