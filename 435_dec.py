from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

AES_KEY = b'Can_decrypt_me_!'
AES_IV = b'1t3f5s7e9t111213'  

def decrypt_input(encrypted_str, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = base64.b64decode(encrypted_str)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted_data.decode()

flag = "xU5cNXeXeIL0aCBw0stJ5Q=="
decrypted_flag = decrypt_input(flag, AES_KEY, AES_IV)
print("Decrypted Flag:", decrypted_flag)
