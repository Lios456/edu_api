import base64
import hmac
import hashlib
from Crypto.Cipher import AES
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class CodeIgniterCrypto:
    def __init__(self, master_key):
        self.master_key = master_key.encode('utf-8')
        self.derive_keys()

    def derive_keys(self):
        hkdf = HKDF(
            algorithm=hashes.SHA512(),
            length=32 + 64,
            salt=None,
            info=b'',
            backend=default_backend()
        )
        derived = hkdf.derive(self.master_key)
        self.encryption_key = derived[:32]
        self.auth_key = derived[32:]

    def encrypt(self, plaintext):
        iv = AES.get_random_bytes(16)
        nonce = iv[:8]
        initial_value = int.from_bytes(iv[8:], 'big')

        cipher = AES.new(
            self.encryption_key,
            AES.MODE_CTR,
            nonce=nonce,
            initial_value=initial_value
        )
        ciphertext = cipher.encrypt(plaintext.encode('utf-8'))

        hmac_value = hmac.new(
            self.auth_key,
            ciphertext + iv,
            hashlib.sha512
        ).digest()

        encrypted_data = iv + ciphertext + hmac_value
        return base64.b64encode(encrypted_data).decode('utf-8')

    def decrypt(self, encrypted_text):
        try:
            decoded = base64.b64decode(encrypted_text)
            iv = decoded[:16]
            hmac_stored = decoded[-64:]
            ciphertext = decoded[16:-64]

            hmac_calculated = hmac.new(
                self.auth_key,
                ciphertext + iv,
                hashlib.sha512
            ).digest()

            if not hmac.compare_digest(hmac_calculated, hmac_stored):
                raise ValueError("HMAC inválido")

            nonce = iv[:8]
            initial_value = int.from_bytes(iv[8:], 'big')

            cipher = AES.new(
                self.encryption_key,
                AES.MODE_CTR,
                nonce=nonce,
                initial_value=initial_value
            )
            plaintext = cipher.decrypt(ciphertext)
            return plaintext.decode('utf-8')

        except Exception as e:
            print(f"Error: {str(e)}")
            return None
