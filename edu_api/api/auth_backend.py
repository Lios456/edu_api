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
        salt=None,  # CI4 no utiliza salt en este caso
        info=info,
        backend=default_backend()
    )
    return hkdf.derive(key)

def decrypt_ci4(data: bytes,
                key: bytes = b"Edu4trol@.#",
                raw_data: bool = True,
                encrypt_key_info: bytes = b'',
                auth_key_info: bytes = b'') -> bytes:
    """
    Desencripta 'data' siguiendo la lógica de CI4.
    
    Se espera que 'data' tenga el siguiente formato:
      HMAC (64 bytes) + IV (16 bytes) + ciphertext.
    """
    digest_size = 64   # SHA512 produce 64 bytes
    iv_length = 16     # Para AES-256-CTR, el IV es de 16 bytes

    # Si los datos están codificados en base64 y raw_data es False, se decodifican.
    if not raw_data:
        data = base64.b64decode(data)

    # Extraer HMAC y el resto del mensaje (IV + ciphertext)
    hmac_extracted = data[:digest_size]
    encrypted_data = data[digest_size:]

    # Derivar la clave de autenticación y recalcular el HMAC
    auth_key = hkdf_derive(key, digest_size, auth_key_info)
    hmac_calculated = hmac.new(auth_key, encrypted_data, hashlib.sha512).digest()

    # Verificar que el HMAC coincide (comparación en tiempo constante)
    if not hmac.compare_digest(hmac_extracted, hmac_calculated):
        raise ValueError("Fallo en la autenticación: HMAC no coincide.")

    # Extraer el IV y el ciphertext
    iv = encrypted_data[:iv_length]
    ciphertext = encrypted_data[iv_length:]

    # Derivar la clave de encriptación y truncarla a 32 bytes para AES-256
    full_encrypt_key = hkdf_derive(key, digest_size, encrypt_key_info)
    encryption_key = full_encrypt_key[:32]

    # Desencriptar con AES-256-CTR
    cipher = Cipher(algorithms.AES(encryption_key), modes.CTR(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return plaintext

if __name__ == "__main__":


    # Dato encriptado almacenado en la base de datos (en base64)
    encrypted_b64 = "R3fjFQBKgKLbJh0KcYcCgGV508vVpWMzoSggeKWkIOdovfTWWZguPNH0TivKB+2KEqX7VLQlBbYPF/WalW69dYlplrJO4Q0Zt+tjAaXHvKYjhbR6Q7Oqi6lqTz4X"
    # Decodificar la cadena base64 para obtener los datos binarios
    encrypted_data = base64.b64decode(encrypted_b64)

    try:
        decrypted = decrypt_ci4(data=encrypted_data, raw_data=True)
        print("Dato desencriptado:", decrypted.decode('utf-8'))
    except Exception as e:
        print("Error durante la desencriptación:", e)
