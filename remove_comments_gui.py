import tkinter as tk
from tkinter import filedialog,messagebox
from remove_comments_cli import process_tex

def open_file_dialog():
    file_paths = filedialog.askopenfilenames()
    processed_files = []
    for file_path in file_paths:
        process_tex(file_path, file_path.rstrip(".tex") + "_NoComments.tex")
        processed_files.append(file_path)
    messagebox.showinfo("Verarbeitete Dateien", "Folgende Dateien wurden verarbeitet:\n" + "\n".join(processed_files))

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  # Wir möchten keine GUI anzeigen, nur den Dateidialog
    open_file_dialog()

