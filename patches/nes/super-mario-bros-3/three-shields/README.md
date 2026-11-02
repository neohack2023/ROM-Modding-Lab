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

## 🧩 Choose a patcher for your device

**Easiest option for most people:** [Rom Patcher JS (opens in your browser)](https://www.marcrobledo.com/RomPatcher.js/). It supports IPS patches and works in modern desktop and mobile browsers. No separate patching app is required.

| Your device | Recommended IPS patcher | How to use it |
|---|---|---|
| **Windows** | [Floating IPS / Flips](https://github.com/royTam1/flips/releases) | Download the Windows version; choose **Apply Patch**. |
| **Mac (macOS)** | [MultiPatch](https://github.com/Sappharad/MultiPatch/releases) | Install the Mac app and apply the `.ips` file to your ROM. |
| **Linux** | [Floating IPS / Flips](https://github.com/royTam1/flips) or [Rom Patcher JS](https://www.marcrobledo.com/RomPatcher.js/) | Use the Linux/GTK build if available, or patch in your browser. |
| **Android** | [UniPatcher on Google Play](https://play.google.com/store/apps/details?id=org.emunix.unipatcher) ([F-Droid alternative](https://f-droid.org/packages/org.emunix.unipatcher/)) | Select the IPS patch, original ROM and output filename, then apply. |
| **iPhone / iPad (iOS/iPadOS)** | [Rom Patcher JS](https://www.marcrobledo.com/RomPatcher.js/) | Use Safari to select both files from Files, tap **Apply patch**, then save the result. |
| **ChromeOS / Chromebook** | [Rom Patcher JS](https://www.marcrobledo.com/RomPatcher.js/) | Use the browser patcher; select your ROM and IPS patch. |

### Quick browser method (works on computers and many phones)

1. [Download the Three Shields IPS patch](SMB3_NES_Three_Shields_v0.2_US_PRG1.ips) and keep your original **USA PRG1** `.nes` file handy.
2. Open [Rom Patcher JS](https://www.marcrobledo.com/RomPatcher.js/).
3. Under **ROM file**, select your original `.nes` game.
4. Under **Patch file**, select our `.ips` patch.
5. Choose **Apply patch**, then save the resulting `.nes` file.
6. Open the new `.nes` game in a compatible NES emulator.

**Important:** A *patcher* creates the modified ROM; an *emulator* plays it. They are separate tools. Some phones may require using the Files app to save or move the patched game. If you get an error or the game acts strangely, verify the original ROM is the **USA PRG1** revision. Don't patch an already modified ROM.

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
