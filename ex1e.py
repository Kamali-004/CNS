import string
import random

ALPHABET = string.ascii_uppercase

#def generate_key(length):
    #return ''.join(random.choice(ALPHABET) for _ in range(length))
def vernam_cipher(text, key):
    cipher_text = []
    for i, char in enumerate(text):
        if char in ALPHABET:
            encrypted_char = chr((ord(char) - 65) ^ (ord(key[i]) - 65) % 26 + 65)
            cipher_text.append(encrypted_char)
        else:
            cipher_text.append(char)
    return ''.join(cipher_text)
plaintext = input("Enter plaintext: ")
key=input("Enter key text: ")
#key = generate_key(len(plaintext))
encrypted_text = vernam_cipher(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Encrypted Text: {encrypted_text}")
