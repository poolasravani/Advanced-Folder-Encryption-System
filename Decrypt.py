import os
from tkinter import messagebox
from aes_security import AESCipher


def decrypt_folder(folder_path, password):
    if not os.path.exists(folder_path):
        messagebox.showerror(
            "Error",
            "Selected folder does not exist!"
        )
        return

    cipher = AESCipher(password)
    decrypted_count = 0

    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "rb") as f:
                        encrypted_data = f.read()

                    decrypted_data = cipher.decrypt(encrypted_data)

                    with open(file_path, "wb") as f:
                        f.write(decrypted_data)

                    decrypted_count += 1

                except Exception:
                    pass

        messagebox.showinfo(
            "Success",
            f"{decrypted_count} file(s) decrypted successfully."
        )

    except Exception as e:
        messagebox.showerror(
            "Decryption Error",
            str(e)
        )

