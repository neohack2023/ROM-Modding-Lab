# Three Shields v0.3 room fix: experimental source patch

**DEBUG ONLY. Do not label as a stable release.** This work targets the **original publicly distributed Three Shields v0.2**, not the experimental GOLD Shields branch. The published PRG0 and PRG1 IPS files remain unchanged.

## Findings

The current v0.2 source resets `$7FCF` (health initialization marker) whenever `Map_Operation != $10`. On returning to gameplay it can erroneously set `$7FCE` to 3 HP. This was reproduced in Mesen with a controlled intermediate scene-state pulse on both PRG0 and PRG1. It does **not** constitute a recorded pipe traversal.

The original shield-display cache `$072A` suppresses drawing when HP has not changed, even after the status-bar PPU tiles are replaced. A controlled tile-clear experiment reproduced missing shields on both revisions. Unconditional and periodic redrawing repaired that synthetic clear, but produced six stray border pixels at a damage-frame screenshot. Those strategies were rejected.

## Preferred event-driven candidate

See [eventdirty03_source.diff](eventdirty03_source.diff), a **source-only** change against our existing non-GOLD disassembly.

- In PRG26, clear HP initialization only on the world-map state `$0D`, not on every non-`$10` state. Other temporary states retain HP.
- In PRG30, intercept the original level-loader `PRG030_8B03` status-bar rebuild, preserve its call to `Video_Do_Update`, then set `$072A = $FF` to force the next shield redraw.
- The new hook is located at CPU `$9FB6` in previously unused PRG30 space. This is not a periodic screen update.

A staged NESASM 3.01 rebuild reproduced the public PRG1 ROM **byte-for-byte before modification**. Both revision-specific experimental ROMs and IPS deltas were generated locally with SHA-256 round-trip checks, **without using any GOLD binaries** and without uploading game ROMs.

## Verified in Mesen 2.2.1

| Test | PRG0 | PRG1 |
| --- | --- | --- |
| Original boot through actual world-map → level loader invokes hook | Pass | Pass |
| Correct shield tiles after native level load | Pass | Pass |
| Real Goomba contact with seeded Fire/Hammer suit | Pass (Fire) | Pass (Hammer) |
| Original question-block mushroom spawn and native pickup | Pass | Pass |
| Native postdeath map → level reentry restores HP 3/3 | Pass | Pass |

The event-driven PRG1 candidate was **pixel-identical to the public v0.2 build at the sampled frame 205** where the periodic strategies showed off-target border changes. Synthetic state pulse and PPU experiments are tracked separately from the actual native level-loader event.

## Release-blocking gaps

- [ ] **Real in-level pipe/bonus-room transition:** HP before/after, correct shields, stable entry and exit.
- [ ] **Actual fortress/boss-room transition:** verify status-bar PPU tiles, MMC3 CHR banks and shield tile graphics.
- [ ] Full parity tests for multiworld, multiple suits, 2-player, and longer play.
- [ ] Pixel comparison during genuine transitions, not only World 1-1 or a synthetic tile clear.
- [ ] Final v0.3 build and release approval after PRG0 **and** PRG1 acceptance.

The event-driven hook is currently verified for the normal level loader. **It has not been demonstrated to fix an arbitrary PPU overwrite or every boss-room loader.** The independent synthetic unthrottled HUD repair must not be confused with this event-driven candidate.

## Reproducibility and provenance

- [Tracking issue #3](https://github.com/neohack2023/ROM-Modding-Lab/issues/3)
- The authoritative local execution records are on Host 02 in `SMB3_HEALTH_BAR_NES_01/evidence/debug_run_20261105`, with local summary `build/V03_ROOMFIX_01/V03_DEBUG_ACCEPTANCE.json`. These contain revision-qualified Mesen event traces.
- Source diff SHA-256: `76cf38b422209e96877840a795cb775e6fb7d8376621f079890f610c4a435c89` (LF text).
- Debug PRG0 ROM SHA-256: `19521d1269c58cf7e0f711e971147c2496bbb018210a492966e0f1414a2699a4`.
- Debug PRG1 ROM SHA-256: `0757e3c29d1b901511f9e636bb5d607b559b76328292336bb2c96bbe653568d0`.
- This repository contains no original ROMs, debug patched ROMs, or unpublished game-binary patches for this experiment.

**Status: partially verified engineering candidate. Not a public v0.3 release.**

## 2026-11-05 update: actual door-transition refill traced and addressed in a new **debug-only** candidate

A player manually reproduced the door bug in Mesen with **2/3 HP before entering and 3/3 afterward**. The passive `manual_door_trace_01/events.tsv` captured, at **frame 65342**, the native `Level_DoChangeReset` loop at PRG5 CPU `$BE3A` clearing **both** `$7FCF` and `$7FCE`. The existing PRG26 HUD initializer immediately refilled HP from zero to three at `$B519`. The loop starts at Y=9, but `SpecialObj_ID` is declared as only eight bytes at `$7FC6–$7FCD`. Y=8 and Y=9 write into the custom HP and initialization marker bytes. This is a compatibility collision between original SMB3's reset-loop behavior and our mod's chosen RAM locations, not proof of an original-game health bug.

**New [bounds-corrected source-only patch](specialobj_bounds04_source.diff):** change `PRG005_BE35: LDY #$09` to `LDY #$07`. Exactly **one ROM byte** at file offset `0xBE46` differs from the prior event-driven candidate. Both PRG0 and PRG1 builds and private debug IPS reconstructions are byte-verified.

**Targeted Mesen old-vs-new tests passed on both PRG0 and PRG1.** With HP=2 and marker `$A5` in a previously verified checkpoint, the engine's real `Level_DoChangeReset` was invoked by setting its `Level_ChangeReset` flag to zero. The old build performed ten special-object clearing iterations and reset HP to three; the corrected build performed eight iterations, **no HP or marker writes**, and kept HP at two for the remaining test frames. This is a **controlled invocation**, not yet a human-played door/pipe rerun of the fixed ROM.

Private candidate SHA-256: PRG0 `01e3051fed11b8dac98ec94919dfb974501c1ab29629c115da9486706dfe5bdb`; PRG1 `369e5cf0f316a89f538fad7923d7c6fe0c5741b7506b5c20ba5e8a116d616467`.

**Release status remains blocked:** Retest the exact door on the corrected build, inspect native boss-room graphics, run broader dual-revision gameplay regression, and only then consider a new public release. Both published v0.2 IPS files remain untouched.
