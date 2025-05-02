def create_caesar_cipher_dicts(shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    encrypt_dict = {original: shifted for original, shifted in zip(alphabet, shifted_alphabet)}
    decrypt_dict = {shifted: original for original, shifted in zip(alphabet, shifted_alphabet)}

    return encrypt_dict, decrypt_dict
def caesar_encrypt(plaintext, encrypt_dict):
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = "".join(encrypt_dict.get(char, char) for char in plaintext)
    return ciphertext
def caesar_decrypt(ciphertext, decrypt_dict):
    ciphertext = ciphertext.upper()
    plaintext = "".join(decrypt_dict.get(char, char) for char in ciphertext)
    return plaintext
shift = int(input("Enter a shift value: "))
plaintext = input("Enter a plaintext: ")
encrypt_dict, decrypt_dict = create_caesar_cipher_dicts(shift)

ciphertext = caesar_encrypt(plaintext, encrypt_dict)
print("Ciphertext:", ciphertext)
decrypted_text = caesar_decrypt(ciphertext, decrypt_dict)
print("Decrypted Text:", decrypted_text)
