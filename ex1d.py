def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper()
    key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    ciphertext = ""

    for p, k in zip(plaintext, key):
        shift = (ord(p) - ord('A') + ord(k) - ord('A')) % 26
        ciphertext += chr(shift + ord('A'))

    return ciphertext


def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    plaintext = ""

    for c, k in zip(ciphertext, key):
        shift = (ord(c) - ord('A') - (ord(k) - ord('A'))) % 26
        plaintext += chr(shift + ord('A'))

    return plaintext
plaintext = input("Enter a plaintext: ")
key = input("Enter a key: ")

ciphertext = vigenere_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = vigenere_decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)
