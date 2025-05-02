import pyDes
import base64

def des_encrypt(plain_text, key):
    
    des = pyDes.des(key, pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)
    encrypted_data = des.encrypt(plain_text)
    return base64.b64encode(encrypted_data).decode()

def des_decrypt(encrypted_text, key):
    
    des = pyDes.des(key, pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)
    encrypted_text = base64.b64decode(encrypted_text)
    return des.decrypt(encrypted_text).decode()

key = input("Enter an 8-character key: ")
while len(key) != 8:
    print("Key must be exactly 8 characters long.")
    key = input("Enter an 8-character key: ")

message = input("Enter the message to encrypt: ")

encrypted_msg = des_encrypt(message, key)
print(f"\nEncrypted Message: {encrypted_msg}")

decrypted_msg = des_decrypt(encrypted_msg, key)
print(f"Decrypted Message: {decrypted_msg}")
