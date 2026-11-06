# Three Shields v0.3: Keep your old saves

**The v0.3 playtest fixes the room-transition shield reset without requiring players to start over.** MesenCE 2.2.1 tests successfully loaded real v0.2 PRG0 and PRG1 save states, plus an earlier PRG1 playtest state, into the corrected v0.3 game. Preserved measurements included shield HP, lives, suit, world/level position and HUD tiles. See [the verification manifest](V03_VERIFICATION.json).

## Before upgrading

1. **Back up your original v0.2 `.nes` and all save-state files.** Do not delete or overwrite the only copy of a state.
2. Apply the matching **v0.3 PRG0 or PRG1 IPS to your original unmodified NES ROM**. Do not stack patches on an already modified ROM. Keep your v0.2 patched ROM as a rollback.
3. In Mesen, open your patched v0.3 game, then use **Ctrl+L** (Load State from File) and select a backup of the old v0.2 `.mss` state. Verify your lives, position, inventory/suit and shields before saving anything new. Mesen default file-load hotkey can be customized.
4. Once the old state loads and runs correctly, save a **new v0.3 state** using **Ctrl+S** (Save State to File) to a **new filename**, leaving the old file intact. Repeat for any states worth keeping.

For automatic **F1–F8 slot** access, Mesen normally organizes slots by the ROM filename. A newly named v0.3 ROM may appear to have no old slots even when the old files still exist. Either use **Ctrl+L** to load the original `.mss`, or back up and copy the old slot file into the new ROM's matching slot filename in Mesen's configured `SaveStates` directory. Don't move or overwrite the original.

Default Windows MesenCE save-state directory on our test installation: `%USERPROFILE%\Documents\MesenCE\SaveStates`. If yours differs, check Mesen's configuration.

## Important limitations

- The **original NES SMB3 ROM has no battery-backed save** flag. Three Shields does not add a cartridge SRAM/save system. "Saves" here means **emulator snapshots** such as Mesen `.mss` files, not an in-game Save menu.
- **Mesen save states are emulator-specific**. Successful migration was directly verified in **MesenCE 2.2.1**. Other emulators, older/newer Mesen formats, cheats, hacks and unusual save states may behave differently. Keep your originals so you can revert.
- **PRG0 states belong to PRG0; PRG1 states belong to PRG1**. Don't mix revisions. GOLD experimental saves are **out of scope**.
- **Room-transition HP fix** is manually verified on PRG1 ordinary and boss-room doors. PRG0 has engine-level automated regression; the full 2-player, all-world and boss HUD test matrix remains open. This is a **playtest release**, not a claim of total compatibility.

## If your save won't load

Try the original v0.2 patch with its original state first, to verify that the state itself still works. If it does, keep the original untouched and report the emulator name/version, PRG0/PRG1, state filename, and any load error in [issue #3](https://github.com/neohack2023/ROM-Modding-Lab/issues/3). Never upload a copyrighted ROM; a screenshot and error message are enough to start troubleshooting.

**We will not delete v0.2.** It remains available as a rollback.
