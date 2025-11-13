````markdown
# Lazy Folder Organizer — How to use

A small, easy-to-use tool to sort files in a folder into category subfolders (Images, Documents, Videos, Music, Archives, Installers, Scripts, Others).

**Prerequisites**
- **Python**: Python 3.8+ installed and available on `PATH`.
- **Optional**: `pyinstaller` if you want to build a single EXE.

**Quick Start (GUI)**

  `python organizer_gui.py`

 **Recommended (easy start):** Double-click `run_gui.bat` to launch the GUI quickly.
 **Hide console:** If you prefer to hide the launcher completely, double-click `run_gui.vbs` (it runs the app with `pythonw`).
 **Run from console:** `python organizer_gui.py`

 In the GUI: paste or browse to the folder to organize, enable **Create if missing** if you want the folder created, then click **Organize**. Click **Show log** to view the actions taken.

 The GUI is intentionally minimal, interactive, and—fun to try. It provides a quick, visual way to see files moved into categories.

**Quick Start (CLI)**
- Run the command-line organizer directly:

  `python organizer.py --path "C:\Path\To\Folder" --create`

- Common options:
  - `--path`, `-p`: Path to the folder to organize. If omitted, `organizer.py` will try to open a native folder picker (requires Tkinter).
  - `--create`: Create the target folder if it does not exist.
  - `--no-gui`: When used without `--path`, prevents opening the folder picker GUI.

- Environment variable: you can set `DOWNLOADS_PATH` to change the default path used by `organizer.py`.

**Create a Windows EXE (optional)**
- Install PyInstaller and build a single-file, windowed EXE:

  ```powershell
  pip install pyinstaller
  cd d:\ALL_DOC\Files-Types-Sorting
  pyinstaller --onefile --windowed organizer_gui.py
  ```

- The EXE will be placed in the `dist\` folder (e.g. `dist\organizer_gui.exe`).

**Project layout**
- `organizer_gui.py`: Minimal Tkinter GUI that calls `organize_folder(path, create_missing, writer)`.
- `organizer.py`: Command-line organizer with `--path`, `--create`, and `--no-gui` options.
- `run_gui.bat`, `run_gui.vbs`: Convenience scripts to launch the GUI (VBScript hides the console).
- `test_downloads/`: Example directories you can use to safely try the organizer.

**Example: test run (safe)**
- Try organizing the included example folder:

  `python organizer.py --path "test_downloads" --create`

- Or point the GUI at `test_downloads` and click **Organize**.

**Safety notes**
- This tool moves files into subfolders. Make a backup if you need to preserve the original layout.
- Files with extensions not matched by the built-in categories are moved into `Others`.
- The category lists are defined in `organizer.py` and `organizer_gui.py` (`FILE_CATEGORIES`) and can be extended if needed.

If you'd like, I can add a small `requirements.txt`, a sample `.exe` build script, or update the categories. Just tell me which.

````
# Lazy Folder Organizer — GUI launcher and packaging

This workspace contains a tiny GUI wrapper `organizer_gui.py` to organize files in a folder.

Quick usage
- Double-click `run_gui.vbs` (recommended) or `run_gui.bat` to launch the app without a console window.
- Paste or browse to the folder you want organized, optionally check "Create if missing", then click "Organize".
- Click "Show log" to view the actions performed.

If you prefer a single EXE, you can create one locally with PyInstaller (optional):

```powershell
pip install pyinstaller
cd path\to\lazy-folder-organizer
pyinstaller --onefile --windowed organizer_gui.py
```

The built EXE will be in `dist\organizer_gui.exe`.

That's it — the GUI is intentionally minimal to keep it easy for anyone to use.
