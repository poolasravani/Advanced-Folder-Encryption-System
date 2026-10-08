import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class AESCipher:

    def __init__(self, password):
        self.key = hashlib.sha256(password.encode()).digest()

    def encrypt(self, data):
        iv = get_random_bytes(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        encrypted_data = cipher.encrypt(
            pad(data, AES.block_size)
        )

        return base64.b64encode(iv + encrypted_data)

    def decrypt(self, encrypted_data):
        encrypted_data = base64.b64decode(encrypted_data)

        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        decrypted_data = unpad(
            cipher.decrypt(ciphertext),
            AES.block_size
        )

        return decrypted_data
