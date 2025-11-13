import os
import shutil
from pathlib import Path

# === CONFIG ===
# Default path (can be overridden with the DOWNLOADS_PATH env var or --path argument)
DEFAULT_DOWNLOADS = Path(r"D:\Download") / "Downloads"
DOWNLOADS_PATH = Path(os.getenv("DOWNLOADS_PATH", str(DEFAULT_DOWNLOADS)))

# Define categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Installers": [".exe", ".msi", ".dmg"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
}

def organize_folder():
    print(f"Organizing files in: {DOWNLOADS_PATH}\n")

    if not DOWNLOADS_PATH.exists():
        print(f"Path not found: {DOWNLOADS_PATH}. Nothing to organize.")
        return

    for file in DOWNLOADS_PATH.iterdir():
        if file.is_file():
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if file.suffix.lower() in extensions:
                    target_dir = DOWNLOADS_PATH / category
                    target_dir.mkdir(exist_ok=True)
                    try:
                        shutil.move(str(file), str(target_dir / file.name))
                        print(f"Moved: {file.name} → {category}/")
                    except Exception as e:
                        print(f"Failed to move {file.name} to {category}: {e}")
                    moved = True
                    break
            if not moved:
                other_dir = DOWNLOADS_PATH / "Others"
                other_dir.mkdir(exist_ok=True)
                try:
                    shutil.move(str(file), str(other_dir / file.name))
                    print(f"Moved: {file.name} → Others/")
                except Exception as e:
                    print(f"Failed to move {file.name} to Others: {e}")

    print("\n✅ Done organizing!")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Organize files in a folder into categories")
    parser.add_argument("--path", "-p", help="Path to folder to organize")
    parser.add_argument("--create", action="store_true", help="Create the path if it doesn't exist")
    parser.add_argument("--no-gui", action="store_true", help="Don't show folder picker GUI when no --path is provided")
    args = parser.parse_args()

    if args.path:
        DOWNLOADS_PATH = Path(args.path)
    else:
        # If no path provided, try to open a native folder picker (tkinter) unless --no-gui was used
        if not args.no_gui:
            try:
                import tkinter as _tk
                from tkinter import filedialog as _filedialog

                _root = _tk.Tk()
                _root.withdraw()
                chosen = _filedialog.askdirectory(title="Select folder to organize")
                _root.destroy()
                if chosen:
                    DOWNLOADS_PATH = Path(chosen)
                else:
                    print("No folder selected. Exiting.")
                    raise SystemExit(0)
            except Exception as e:
                print(f"Could not open folder picker GUI: {e}")
                print("Run with --path <folder> or --no-gui to avoid GUI.")
                raise

    # If path does not exist, optionally create it (useful for first-run)
    if not DOWNLOADS_PATH.exists():
        if args.create:
            try:
                DOWNLOADS_PATH.mkdir(parents=True, exist_ok=True)
                print(f"Created missing path: {DOWNLOADS_PATH}")
            except Exception as e:
                print(f"Failed to create path {DOWNLOADS_PATH}: {e}")
                raise
        else:
            print(f"Error: path {DOWNLOADS_PATH} does not exist. Use --create to create it or pass a valid --path.")
            raise SystemExit(1)

    organize_folder()
