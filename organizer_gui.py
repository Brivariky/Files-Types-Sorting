"""A very small, simple GUI for organizing a folder.

Keep it minimal: paste a folder path or browse, optional create-if-missing,
and click Organize. The log is hidden by default; users can toggle it.
This file intentionally avoids extra features so it's easy to use.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from pathlib import Path
import shutil


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Installers": [".exe", ".msi", ".dmg"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
}


def organize_folder(path: Path, create_missing: bool = False, writer=None):
    if not path.exists():
        if create_missing:
            path.mkdir(parents=True, exist_ok=True)
            if writer:
                writer(f"Created: {path}")
        else:
            if writer:
                writer("Path not found. Nothing to do.")
            return

    for item in path.iterdir():
        if item.is_file():
            moved = False
            for cat, exts in FILE_CATEGORIES.items():
                if item.suffix.lower() in exts:
                    dest = path / cat
                    dest.mkdir(exist_ok=True)
                    try:
                        shutil.move(str(item), str(dest / item.name))
                        if writer:
                            writer(f"Moved: {item.name} → {cat}/")
                    except Exception as e:
                        if writer:
                            writer(f"Failed: {item.name}: {e}")
                    moved = True
                    break
            if not moved:
                dest = path / "Others"
                dest.mkdir(exist_ok=True)
                try:
                    shutil.move(str(item), str(dest / item.name))
                    if writer:
                        writer(f"Moved: {item.name} → Others/")
                except Exception as e:
                    if writer:
                        writer(f"Failed: {item.name}: {e}")


class SimpleGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Folder Organizer")
        self.resizable(False, False)
        self._build()

    def _build(self):
        pad = 8
        frm = tk.Frame(self, padx=pad, pady=pad)
        frm.pack()

        tk.Label(frm, text="Folder:").grid(row=0, column=0, sticky="w")
        self.path_var = tk.StringVar()
        e = tk.Entry(frm, textvariable=self.path_var, width=60)
        e.grid(row=1, column=0, columnspan=2, pady=(4, 8))

        tk.Button(frm, text="Browse", command=self._browse).grid(row=1, column=2, padx=(6,0))

        self.create_var = tk.BooleanVar(value=False)
        tk.Checkbutton(frm, text="Create if missing", variable=self.create_var).grid(row=2, column=0, sticky="w")

        tk.Button(frm, text="Organize", command=self._organize).grid(row=3, column=0, pady=(8,0), sticky="w")
        tk.Button(frm, text="Quit", command=self.destroy).grid(row=3, column=2, pady=(8,0), sticky="e")

        # Hidden log
        self.log_shown = False
        self.log = scrolledtext.ScrolledText(self, height=10, width=80, state="disabled")
        tk.Button(frm, text="Show log", command=self._toggle_log).grid(row=2, column=2, sticky="e")

    def _browse(self):
        d = filedialog.askdirectory()
        if d:
            self.path_var.set(d)

    def _write(self, line: str):
        self.log.configure(state="normal")
        self.log.insert("end", line + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def _organize(self):
        path = Path(self.path_var.get().strip())
        # clear log
        self.log.configure(state="normal")
        self.log.delete("1.0", "end")
        self.log.configure(state="disabled")
        organize_folder(path, create_missing=self.create_var.get(), writer=self._write)
        messagebox.showinfo("Done", "Organizing finished.")

    def _toggle_log(self):
        if not self.log_shown:
            self.log.pack(padx=8, pady=(0,8))
            self.log_shown = True
        else:
            self.log.pack_forget()
            self.log_shown = False


if __name__ == "__main__":
    SimpleGUI().mainloop()
