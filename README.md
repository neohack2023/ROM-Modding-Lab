# ROM Modding Lab 🎮

**Game mods, patches, and tools for classic consoles.**

This is where I share playable ROM hacks and the tools used to build and test them. You can download the small patch files here, apply them to **your own game**, and play in an emulator.

## 🕹️ Play a mod

### Super Mario Bros. 3 (NES): Three Shields v0.2

**Give Mario three shields instead of relying only on his usual power-up health.**

- Getting hit removes one shield.
- Mushrooms restore a shield.
- Lose all three and Mario dies normally.
- Mario's usual movement and power-up animations remain part of the game.

**[➡️ Download, install, and play Three Shields](patches/nes/super-mario-bros-3/three-shields/README.md)**

**Works with:** original NES Super Mario Bros. 3 **(USA PRG1)**. Not the SNES All-Stars edition.

This is a community playtest version. More levels, suits and two-player situations still need testing.

## ❓ What is a ROM patch?

A patch is a **small file containing only the changes** to a game. To play it, you provide your own compatible game ROM, apply the patch using a patcher, and then open the resulting game file in an emulator.

You do **not** download full commercial games from this repository. Each mod page explains exactly which game version it needs.

## 🛠️ Building the lab

The collection is designed to expand across NES, SNES, N64 and other classic systems.

| Area | What belongs here |
|---|---|
| `patches/` | Downloadable game patches with simple instructions |
| `tools/` | Reusable patch-building and verification scripts |
| `docs/` (planned) | Modding guides and technical notes |
| `manifests/` (planned) | Game-version and patch compatibility records |

[Report a problem or suggest a mod](https://github.com/neohack2023/ROM-Modding-Lab/issues)

**No commercial ROMs or BIOS files are distributed here.** Full verification hashes and developer details are at the bottom of each mod's page.
