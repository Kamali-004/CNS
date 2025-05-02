def create_key_square(keyword):
    keyword = keyword.upper().replace('J', 'I')
    key_square = []
    used_chars = set()
    for char in keyword:
        if char not in used_chars and char.isalpha():
            key_square.append(char)
            used_chars.add(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used_chars:
            key_square.append(char)

    return [key_square[i:i + 5] for i in range(0, 25, 5)]


def prepare_text(text):
    text = text.upper().replace('J', 'I').replace(' ', '')
    prepared = []
    i = 0

    while i < len(text):
        pair = text[i]
        if i + 1 < len(text) and text[i] != text[i + 1]:
            pair += text[i + 1]
            i += 2
        else:
            pair += 'X'
            i += 1
        prepared.append(pair)

    return prepared


def find_position(char, key_square):
    for row, line in enumerate(key_square):
        if char in line:
            return row, line.index(char)
    return None


def playfair_cipher(text_pairs, key_square, mode='encrypt'):
    shift = 1 if mode == 'encrypt' else -1
    result = []

    for pair in text_pairs:
        r1, c1 = find_position(pair[0], key_square)
        r2, c2 = find_position(pair[1], key_square)

        if r1 == r2:
            result.append(key_square[r1][(c1 + shift) % 5])
            result.append(key_square[r2][(c2 + shift) % 5])
        elif c1 == c2:
            result.append(key_square[(r1 + shift) % 5][c1])
            result.append(key_square[(r2 + shift) % 5][c2])
        else:
            result.append(key_square[r1][c2])
            result.append(key_square[r2][c1])

    return ''.join(result)

keyword = input("Enter Keyword: ")
plaintext = input("Enter Plaintext: ")

key_square = create_key_square(keyword)
print("Key Square:")
for row in key_square:
    print(row)

prepared_text = prepare_text(plaintext)
print("\nPrepared Text:", prepared_text)

ciphertext = playfair_cipher(prepared_text, key_square, mode='encrypt')
print("\nCiphertext:", ciphertext)

decrypted_text = playfair_cipher(prepare_text(ciphertext), key_square, mode='decrypt')
print("\nDecrypted Text:", decrypted_text)

