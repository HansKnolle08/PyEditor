import tkinter as tk
from tkinter import filedialog, messagebox
import os

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Unbenannt - Texteditor")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Textdateien", "*.txt"), ("Alle Dateien", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"{file_path} - Texteditor")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textdateien", "*.txt"), ("Alle Dateien", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"{file_path} - Texteditor")

def exit_editor():
    if messagebox.askokcancel("Beenden", "Möchten Sie den Editor wirklich verlassen?"):
        root.destroy()

def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def bold_text():
    current_tags = text_area.tag_names("sel.first")
    if "bold" in current_tags:
        text_area.tag_remove("bold", "sel.first", "sel.last")
    else:
        text_area.tag_add("bold", "sel.first", "sel.last")
        text_area.tag_config("bold", font=("Arial", font_size, "bold"))

def italic_text():
    current_tags = text_area.tag_names("sel.first")
    if "italic" in current_tags:
        text_area.tag_remove("italic", "sel.first", "sel.last")
    else:
        text_area.tag_add("italic", "sel.first", "sel.last")
        text_area.tag_config("italic", font=("Arial", font_size, "italic"))

def underline_text():
    current_tags = text_area.tag_names("sel.first")
    if "underline" in current_tags:
        text_area.tag_remove("underline", "sel.first", "sel.last")
    else:
        text_area.tag_add("underline", "sel.first", "sel.last")
        text_area.tag_config("underline", font=("Arial", font_size, "underline"))

def change_font_size(event=None):
    global font_size
    font_size = int(font_size_var.get())
    text_area.config(font=("Arial", font_size))

root = tk.Tk()
root.title("Erweiterter Texteditor")
root.state("normal")

icon_path = os.path.join(os.path.dirname(__file__), "resources", "icon.ico")
try:
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"Warnung: Icon konnte nicht geladen werden. Grund: {e}")

font_size = 14

text_area = tk.Text(root, wrap=tk.WORD, undo=True, font=("Arial", font_size))
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Datei", menu=file_menu)
file_menu.add_command(label="Neu", command=new_file)
file_menu.add_command(label="Öffnen", command=open_file)
file_menu.add_command(label="Speichern", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Beenden", command=exit_editor)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Bearbeiten", menu=edit_menu)
edit_menu.add_command(label="Ausschneiden", command=cut_text)
edit_menu.add_command(label="Kopieren", command=copy_text)
edit_menu.add_command(label="Einfügen", command=paste_text)

format_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Fett", command=bold_text)
format_menu.add_command(label="Kursiv", command=italic_text)
format_menu.add_command(label="Unterstrichen", command=underline_text)

font_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Schriftgröße", menu=font_menu)

font_size_var = tk.StringVar(value=str(font_size))
font_sizes = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 40, 48, 56, 72]
for size in font_sizes:
    font_menu.add_radiobutton(label=str(size), variable=font_size_var, command=change_font_size)

root.mainloop()
