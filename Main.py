import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt import encrypt_folder
from decrypt import decrypt_folder


def browse_folder():
    folder = filedialog.askdirectory()
    folder_var.set(folder)


def encrypt_action():
    folder = folder_var.get()
    password = password_entry.get()

    if folder == "":
        messagebox.showerror("Error", "Please Select Folder")
        return

    if password == "":
        messagebox.showerror("Error", "Please Enter Password")
        return

    encrypt_folder(folder, password)


def decrypt_action():
    folder = folder_var.get()
    password = password_entry.get()

    if folder == "":
        messagebox.showerror("Error", "Please Select Folder")
        return

    if password == "":
        messagebox.showerror("Error", "Please Enter Password")
        return

    decrypt_folder(folder, password)


root = tk.Tk()
root.title("Advanced Folder Encryption System")
root.geometry("550x450")
root.configure(bg="white")
root.resizable(False, False)

folder_var = tk.StringVar()

title = tk.Label(
    root,
    text="Advanced Folder Encryption System",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="blue"
)
title.pack(pady=20)

tk.Label(
    root,
    text="Folder Path",
    bg="white",
    font=("Arial", 11)
).pack()

frame = tk.Frame(root, bg="white")
frame.pack(pady=5)

folder_entry = tk.Entry(
    frame,
    textvariable=folder_var,
    width=40
)
folder_entry.pack(side=tk.LEFT, padx=5)

browse_button = tk.Button(
    frame,
    text="Browse",
    command=browse_folder
)
browse_button.pack(side=tk.LEFT)

tk.Label(
    root,
    text="Password",
    bg="white",
    font=("Arial", 11)
).pack(pady=15)

password_entry = tk.Entry(
    root,
    show="*",
    width=35
)
password_entry.pack()

encrypt_btn = tk.Button(
    root,
    text="Encrypt Folder",
    command=encrypt_action,
    bg="green",
    fg="white",
    width=20
)
encrypt_btn.pack(pady=15)

decrypt_btn = tk.Button(
    root,
    text="Decrypt Folder",
    command=decrypt_action,
    bg="blue",
    fg="white",
    width=20
)
decrypt_btn.pack()

exit_btn = tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    bg="red",
    fg="white",
    width=20
)
exit_btn.pack(pady=20)

root.mainloop()
