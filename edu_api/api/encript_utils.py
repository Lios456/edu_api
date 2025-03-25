# encryption_utils.py
import base64
import hmac
import hashlib
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def hkdf_derive(key: bytes, length: int, info: bytes = b'') -> bytes:
    """
    Deriva una clave usando HKDF con SHA512.
    """
    hkdf = HKDF(
        algorithm=hashes.SHA512(),
        length=length,
        salt=None,  # Sin salt, igual que CI4
        info=info,
        backend=default_backend()
    )
    return hkdf.derive(key)

def decrypt_ci4(data: bytes, key: bytes, raw_data: bool = True,
                encrypt_key_info: bytes = b'', auth_key_info: bytes = b'') -> bytes:
    """
    Desencripta 'data' siguiendo la lógica de CodeIgniter 4.
    
    Se espera que 'data' tenga el siguiente formato:
      HMAC (64 bytes) + IV (16 bytes) + ciphertext.
    """
    digest_size = 64   # SHA512 produce 64 bytes
    iv_length = 16     # Para AES-256-CTR

    # Extraer el HMAC y el resto del mensaje
    hmac_extracted = data[:digest_size]
    encrypted_data = data[digest_size:]

    # Derivar la clave de autenticación y recalcular el HMAC
    auth_key = hkdf_derive(key, digest_size, auth_key_info)
    hmac_calculated = hmac.new(auth_key, encrypted_data, hashlib.sha512).digest()
    if not hmac.compare_digest(hmac_extracted, hmac_calculated):
        raise ValueError("Fallo en la autenticación: HMAC no coincide.")

    # Extraer el IV y el ciphertext
    iv = encrypted_data[:iv_length]
    ciphertext = encrypted_data[iv_length:]

    # Derivar la clave de encriptación y truncarla a 32 bytes para AES-256
    full_encrypt_key = hkdf_derive(key, digest_size, encrypt_key_info)
    encryption_key = full_encrypt_key[:32]

    cipher = Cipher(algorithms.AES(encryption_key), modes.CTR(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

def encrypt_ci4(plaintext: bytes,
                key: bytes,
                cipher_name: str = 'AES-256-CTR',
                digest_name: str = 'SHA512',
                raw_data: bool = True,
                encrypt_key_info: bytes = b'',
                auth_key_info: bytes = b'') -> bytes:
    """
    Cifra 'plaintext' siguiendo la lógica de CodeIgniter 4.
    
    Pasos:
      1. Deriva la clave de encriptación usando HKDF con SHA512, truncándola a 32 bytes para AES-256.
      2. Genera un IV aleatorio de 16 bytes.
      3. Cifra el plaintext usando AES-256-CTR con el IV.
      4. Concatena IV y ciphertext.
      5. Deriva la clave de autenticación y calcula el HMAC (64 bytes) sobre (IV + ciphertext) con SHA512.
      6. Devuelve el mensaje final: HMAC + IV + ciphertext.
    
    Si raw_data es False, se retorna el resultado codificado en base64.
    """
    if digest_name.upper() != 'SHA512':
        raise ValueError("Solo se soporta SHA512")
    
    digest_size = 64     # SHA512 produce 64 bytes
    iv_length = 16       # Para AES-256-CTR, IV de 16 bytes

    # Derivar la clave de encriptación (64 bytes) y truncarla a 32 bytes para AES-256
    full_encrypt_key = hkdf_derive(key, digest_size, encrypt_key_info)
    encryption_key = full_encrypt_key[:32]

    # Generar un IV aleatorio
    iv = os.urandom(iv_length)

    # Cifrar usando AES-256-CTR
    cipher = Cipher(algorithms.AES(encryption_key), modes.CTR(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Concatenar IV y ciphertext
    encrypted_data = iv + ciphertext

    # Derivar la clave de autenticación
    auth_key = hkdf_derive(key, digest_size, auth_key_info)
    # Calcular HMAC sobre (IV + ciphertext)
    hmac_calculated = hmac.new(auth_key, encrypted_data, hashlib.sha512).digest()

    # Mensaje final: HMAC + IV + ciphertext
    final_data = hmac_calculated + encrypted_data

    if raw_data:
        return final_data
    else:
        return base64.b64encode(final_data)
