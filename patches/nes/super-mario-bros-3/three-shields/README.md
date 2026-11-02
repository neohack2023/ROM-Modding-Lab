# SMB3 NES: Three Shields v0.2

A three-shield health system for the **original NES Super Mario Bros. 3 (USA PRG1)**. Not compatible with SNES Super Mario All-Stars or unverified game revisions.

## Features

- Three independent HP shields, displayed using native NES 2bpp HUD graphics.
- Nonfatal damage removes one shield, retaining native invulnerability behavior.
- Native Big Mario shrink and power-up downgrade routines are preserved.
- Mushroom pickup heals one HP (maximum 3), while native growth continues.
- At zero HP, SMB3's normal death sequence runs.
- Shields are hidden on the world map; tested level reentry restores three.

## Installation

1. Back up your own legally sourced **Super Mario Bros. 3 (USA) (PRG1)** NES ROM.
2. Confirm its full-file SHA-256 is `4377a7f5e6eb50bdd2ac6f249bf1a7085500aca8eb41f38545c3a2731c51a579`.
3. Apply `SMB3_NES_Three_Shields_v0.2_US_PRG1.ips` with a standard IPS patcher, to a *copy* of the matching ROM.
4. Open in Mesen or another NES MMC3-compatible emulator.
5. The patched ROM SHA-256 must be `fa84a7f83d1a72639c5e1b270ac160cb2706b31807200cce26a1ddf7f5b8b7ce`.

## QA

Our verified Playtest 02 Mesen fixtures passed small-hit survival, Big Mario shrink, normal final-hit death, native question-block mushroom healing, all 3/2/1/0 shield states, world-map stock pixel parity in sampled frames, and level reentry reset. User playtesting is also reported.

### Known limitations

Not exhaustively validated across all worlds, all suits, two-player/Luigi, pipes, bonus rooms, alternate HUD states or long-play memory conditions. WRAM $072A holds the last-rendered-HP cache. This is a **community playtest release**, not a universal compatibility guarantee.

## Integrity

IPS SHA-256: `ad4b65ab564ef3dddc26dfee9cca89617fddb5cd06af2e4b108742dcf031255d` (7,225 bytes).

The verified source ROM and the already-tested patch round-trip byte-for-byte. No original game ROM is distributed.
