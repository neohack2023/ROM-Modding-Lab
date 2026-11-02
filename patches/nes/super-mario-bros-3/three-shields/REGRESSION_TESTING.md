# Three Shields: regression testing checklist

Help test **both NES USA revisions** of the Three Shields v0.2 mod. This is a practical to-do list for players and contributors. The PRG0 port has passed the core automated checks, but many real-play scenarios remain open.

**Choose the patch matching your original ROM:**
- **USA PRG0 / Rev 0:** `SMB3_NES_Three_Shields_v0.2_US_PRG0_PLAYTEST.ips`
- **USA PRG1 / Rev 1:** `SMB3_NES_Three_Shields_v0.2_US_PRG1.ips`

See [download and installation instructions](README.md) for ROM hashes and patchers. Do not upload commercial ROMs.

## Status key

- `[x]` = previously verified by the recorded Mesen regression (not a claim about every emulator or every level)
- `[ ]` = needs testing and evidence
- Test each open item **separately on PRG0 and PRG1**. Passing one revision doesn't close the other.

## A. Core functionality (previously verified in Mesen)

| Check | PRG0 | PRG1 | Expected behavior |
|---|---|---|---|
| Enemy hit while Small Mario | [x] | [x] | 3 to 2 shields, one hit, no life lost, temporary invulnerability |
| Final shield lost | [x] | [x] | Native death and exactly one life lost |
| Big Mario takes damage | [x] | [x] | Lose one shield, native shrinking animation |
| Mushroom restores a shield | [x] | [x] | HP 2 to 3 without breaking normal growth |
| Mushroom at full HP | [x] | [x] | HP remains capped at 3 |
| Original question block produces mushroom | [x] | [x] | Native pickup path works |
| Shield HUD shows 3 / 2 / 1 / 0 | [x] | [x] | Correct filled/empty heart tiles |
| World map restores original border | [x] | [x] | No shield artifacts on sampled world-map frames |
| Death -> map -> level reentry | [x] | [x] | Three shields restored on a new attempt |

These checks cover controlled fixtures; extended playtesting is still needed.

## B. Power-ups and suits: high priority

| Test | PRG0 | PRG1 | Expected behavior |
|---|---|---|---|
| Fire Mario takes one nonfatal hit | [ ] | [ ] | HP decreases by 1; native power-up downgrade |
| Raccoon Mario takes damage | [ ] | [ ] | HP decreases by 1; native downgrade and tail behavior |
| Frog Suit damaged | [ ] | [ ] | Native suit-loss behavior; no stuck animation |
| Tanooki Suit damaged | [ ] | [ ] | Native downgrade; statue mode remains safe |
| Hammer Suit damaged | [ ] | [ ] | Native downgrade; hammer state resets normally |
| Super Star invincibility | [ ] | [ ] | No HP damage during star invincibility |
| Repeated enemy hits | [ ] | [ ] | Invulnerability window prevents double-decrement |
| Mushroom after other suit transitions | [ ] | [ ] | HP heals by at most one; no unexpected suit change |

## C. Level transitions and special rooms: high priority

| Test | PRG0 | PRG1 | Expected behavior |
|---|---|---|---|
| Enter and exit horizontal pipe | [ ] | [ ] | Current HP survives pipe transition |
| Enter and exit vertical pipe | [ ] | [ ] | HP and HUD remain correct |
| Enter a bonus room, then leave | [ ] | [ ] | HP persists; no HUD flicker |
| Enter a hidden room | [ ] | [ ] | No unintended reset or corrupted graphics |
| Finish a level normally | [ ] | [ ] | No softlock; map returns to normal |
| Enter the next level | [ ] | [ ] | New level starts with three shields |
| Die in a special room | [ ] | [ ] | Native death and map return |
| Pause/resume during transition | [ ] | [ ] | No lost controls, HUD corruption or extra damage |

## D. Two-player mode: high priority

| Test | PRG0 | PRG1 | Expected behavior |
|---|---|---|---|
| Start 2-player game | [ ] | [ ] | Game boots and selects players normally |
| Mario -> Luigi turn switch | [ ] | [ ] | No HP leakage or stale HUD |
| Luigi takes a hit | [ ] | [ ] | Same three-shield damage rules |
| Luigi collects mushroom | [ ] | [ ] | Restores one HP; original growth |
| Luigi dies -> Mario turn | [ ] | [ ] | Lives and HP properly separated |
| Multiple turn changes | [ ] | [ ] | No RAM persistence bug or softlock |

## E. Long-play and world coverage

- [ ] **PRG0:** World 1 full playthrough, including fortress and world exit.
- [ ] **PRG1:** World 1 full playthrough, including fortress and world exit.
- [ ] **PRG0:** Worlds 2–8 smoke tests (at least one level plus transition per world).
- [ ] **PRG1:** Worlds 2–8 smoke tests (at least one level plus transition per world).
- [ ] **PRG0:** 30+ minutes of continuous play, repeated deaths and power-ups.
- [ ] **PRG1:** 30+ minutes of continuous play, repeated deaths and power-ups.
- [ ] **PRG0:** Save/reopen emulator state, confirm HP and HUD.
- [ ] **PRG1:** Save/reopen emulator state, confirm HP and HUD.

## F. Graphics and emulator compatibility

- [ ] **PRG0:** Watch for flicker or stray pixels during fast movement and transitions.
- [ ] **PRG1:** Watch for flicker or stray pixels during fast movement and transitions.
- [ ] **PRG0:** Check HUD alignment on a different NES emulator.
- [ ] **PRG1:** Check HUD alignment on a different NES emulator.
- [ ] **Both:** Test on real NES hardware or accurate flash-cart setup if available.
- [ ] **Both:** Validate no unusual audio glitches, softlocks, or control problems.

## How to report a result

[Open a testing issue](https://github.com/neohack2023/ROM-Modding-Lab/issues/new) with this template:

```text
ROM revision: USA PRG0 / USA PRG1
Patch filename:
Emulator and version:
Platform:
World / level / room:
Power-up or suit:
Checklist item:
Result: PASS / FAIL / NOT TESTED
Reproduction steps:
Expected:
Actual:
Screenshot/video or event log (optional):
```

**Do not mark a checkbox complete for both versions based on a single test.**
Prefer a reproducible failure report over guessing. A successful run in a single emulator doesn't guarantee compatibility everywhere.

## Release gate

Before changing PRG0 from **community playtest** to a stable release, aim to pass all high-priority suit, room-transition, and two-player tests on PRG0, repeat representative tests on PRG1, and complete extended gameplay across multiple worlds. Keep any unresolved issues visibly listed rather than marking them passed.
