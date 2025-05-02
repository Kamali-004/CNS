def rail_fence_encrypt(plaintext, rails):
    if rails <= 1:
        return plaintext  # No change if rails is 1

    rail_pattern = [['\n' for _ in range(len(plaintext))] for _ in range(rails)]
    direction_down = False
    row, col = 0, 0

    for char in plaintext:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        rail_pattern[row][col] = char
        col += 1
        row += 1 if direction_down else -1

    ciphertext = ''.join(rail_pattern[i][j] for i in range(rails) for j in range(len(plaintext)) if rail_pattern[i][j] != '\n')
    return ciphertext

def rail_fence_decrypt(ciphertext, rails):
    if rails <= 1:
        return ciphertext  # No change if rails is 1

    rail_pattern = [['\n' for _ in range(len(ciphertext))] for _ in range(rails)]
    direction_down = None
    row, col = 0, 0

    for _ in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False

        rail_pattern[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if rail_pattern[i][j] == '*' and index < len(ciphertext):
                rail_pattern[i][j] = ciphertext[index]
                index += 1

    plaintext = []
    row, col = 0, 0
    for _ in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False

        if rail_pattern[row][col] != '\n':
            plaintext.append(rail_pattern[row][col])
            col += 1

        row += 1 if direction_down else -1

    return ''.join(plaintext)

if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    rails = int(input("Enter the number of rails: "))

    encrypted_text = rail_fence_encrypt(plaintext, rails)
    decrypted_text = rail_fence_decrypt(encrypted_text, rails)

    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")
