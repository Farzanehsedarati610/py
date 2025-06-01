from Crypto.Cipher import AES
import os

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return cipher.nonce, ciphertext, tag

def decrypt_data(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()

# Example usage
key = os.urandom(16) # Generate random encryption key
nonce, encrypted, tag = encrypt_data("Sensitive Transaction Data", key)
print(f"Encrypted Data: {encrypted}")
print(f"Decrypted Data: {decrypt_data(nonce, encrypted, tag, key)}")

