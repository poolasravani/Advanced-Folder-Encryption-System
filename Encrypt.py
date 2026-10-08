import os
from tkinter import messagebox
from aes_security import AESCipher


def encrypt_folder(folder_path, password):
    if not os.path.exists(folder_path):
        messagebox.showerror(
            "Error",
            "Selected folder does not exist!"
        )
        return

    cipher = AESCipher(password)
    encrypted_count = 0

    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "rb") as f:
                        data = f.read()

                    encrypted_data = cipher.encrypt(data)

                    with open(file_path, "wb") as f:
                        f.write(encrypted_data)

                    encrypted_count += 1

                except Exception:
                    pass

        messagebox.showinfo(
            "Success",
            f"{encrypted_count} file(s) encrypted successfully."
        )

    except Exception as e:
        messagebox.showerror(
            "Encryption Error",
            str(e)
        )
