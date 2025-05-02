import numpy as np
def char_to_num(char):
    return ord(char.upper()) - ord('A')
def num_to_char(num):
    return chr(num + ord('A'))
def text_to_vector(text):
    return [char_to_num(char) for char in text]
def vector_to_text(vector):
    return ''.join(num_to_char(num % 26) for num in vector)
def hill_encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]
    plaintext = plaintext.replace(" ", "").upper()
    if len(plaintext) % n != 0:
        plaintext += 'X' * (n - len(plaintext) % n)
    plaintext_vector = text_to_vector(plaintext)
    ciphertext = ""
    for i in range(0, len(plaintext_vector), n):
        block = np.array(plaintext_vector[i:i + n])
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext += vector_to_text(encrypted_block)

    return ciphertext
def hill_decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    det = int(round(np.linalg.det(key_matrix))) % 26
    det_inv = pow(det, -1, 26)
    adjoint = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    key_inverse = (det_inv * adjoint) % 26
    ciphertext_vector = text_to_vector(ciphertext)
    plaintext = ""
    for i in range(0, len(ciphertext_vector), n):
        block = np.array(ciphertext_vector[i:i + n])
        decrypted_block = np.dot(key_inverse, block) % 26
        plaintext += vector_to_text(decrypted_block)

    return plaintext
key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]  # 3x3 key matrix
key_matrix = np.array(key)

plaintext =input("Enter a plaintext : ")
ciphertext = hill_encrypt(plaintext, key_matrix)
print("Ciphertext:", ciphertext)

decrypted_text = hill_decrypt(ciphertext, key_matrix)
print("Decrypted Text:", plaintext
      )
