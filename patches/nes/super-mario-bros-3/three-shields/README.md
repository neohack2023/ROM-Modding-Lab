# Super Mario Bros. 3 (NES): Three Shields 🛡️

**A simple health-bar mod for the original NES Super Mario Bros. 3.**

Instead of losing a life on an ordinary hit as Small Mario, you get **three shields**. Enemies remove one shield at a time. Collect a mushroom to get one back. Run out of shields and Mario dies as usual.

**Version:** 0.2 (community playtest)  
**Game:** Super Mario Bros. 3, **USA PRG1**, for the **original NES**  
**Play with:** [Mesen](https://www.mesen.ca/) or another NES emulator that runs SMB3

> **This is a patch, not a full game.** You need your own matching copy of Super Mario Bros. 3. It does **not** work with Super Mario All-Stars on SNES.

## ⬇️ Download the patch

### [Download Three Shields v0.2 (.ips)](SMB3_NES_Three_Shields_v0.2_US_PRG1.ips)

If the link opens a GitHub file page instead of downloading, tap the **download icon** or **View raw**.

## 🎮 How to get it running

You need three things:

1. Your own unmodified **Super Mario Bros. 3 (USA) (PRG1)** NES ROM (a `.nes` file).
2. The **Three Shields .ips patch** from the link above.
3. An IPS patching app, such as [Floating IPS (Flips)](https://www.romhacking.net/utilities/1040/), plus an NES emulator such as Mesen.

**On a Windows PC:**

1. Download the `.ips` file above.
2. Open Floating IPS and choose **Apply Patch**.
3. Select the downloaded **Three Shields .ips** file.
4. Select your **original SMB3 USA PRG1 .nes** file.
5. Choose a new output filename, such as `SMB3-Three-Shields.nes`, so your original stays safe.
6. Open the **new** `.nes` file in Mesen, then press **Start** and play normally.

**Already using an emulator?** It is not enough to put the `.ips` into Mesen as a game. First apply the patch to your ROM using the patching app; then open the resulting `.nes` file.

**On a phone:** You still need an IPS patching tool compatible with your phone and an NES emulator. Apply the patch to the correct original game file, then open the patched `.nes` in your emulator. These Windows steps refer specifically to Floating IPS.

## ❤️ How the shields work

| What happens | Result |
|---|---|
| Start a fresh level attempt | 3 full shields |
| Take a hit | Lose 1 shield and get temporary invulnerability |
| Pick up a normal mushroom | Recover 1 shield, up to 3; Mario still grows normally |
| Get hit as Big Mario | Lose 1 shield and shrink through the familiar animation |
| Lose your final shield | Normal SMB3 death animation and life loss |
| Return to the world map | Original map display, no shield icons |

You don't need special button combinations or a separate game menu. **Play SMB3 as you normally would.** Shields appear in the bottom status area while playing levels.

## ✅ What we've tested

The v0.2 patch is based on our playtested NES build. Mesen tests passed for damage, mushroom pickup and healing, normal death, Big Mario shrinking, the shield display at 3/2/1/0, and returning from the world map into a level. We also compared sample screenshots to check for unintended HUD changes.

**Still looking for community testing:** other worlds, Luigi/two-player, special suits, pipes, bonus rooms, and long sessions. It is a **playtest release**, not a promise that every possible scene has been checked.

## 🐛 Found a bug?

[Open a GitHub issue](https://github.com/neohack2023/ROM-Modding-Lab/issues/new) and tell us:
- Which emulator and version you use
- Which world/level and which Mario power-up
- What you did and what went wrong
- A screenshot or short recording, if possible

Please **do not upload commercial ROM files** in bug reports.

## 🔧 Technical details (optional)

You can skip this section if the game runs correctly.

| Item | SHA-256 |
|---|---|
| Required original ROM (USA PRG1) | `4377a7f5e6eb50bdd2ac6f249bf1a7085500aca8eb41f38545c3a2731c51a579` |
| Three Shields v0.2 IPS patch | `ad4b65ab564ef3dddc26dfee9cca89617fddb5cd06af2e4b108742dcf031255d` |
| Resulting patched NES ROM | `fa84a7f83d1a72639c5e1b270ac160cb2706b31807200cce26a1ddf7f5b8b7ce` |

These checksums identify the exact revision we tested. If the patch doesn't work, the most common first thing to check is whether your original ROM matches **USA PRG1**, rather than PRG0 or another revision.

This download contains patch changes only. It does not include the original game.
