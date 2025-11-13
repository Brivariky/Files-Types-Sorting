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
