def encrypt_message(message, num_columns, column_order):
    message = message.replace(" ", "")  # Remove spaces
    message_length = len(message)

    # Add padding if necessary
    while message_length % num_columns != 0:
        message += "X"
        message_length += 1

    # Create grid
    grid = [message[i:i+num_columns] for i in range(0, message_length, num_columns)]

    # Read columns in the specified order
    encrypted_message = ""
    for col in column_order:
        col -= 1  # Convert 1-based index to 0-based
        for row in grid:
            encrypted_message += row[col]

    return encrypted_message

def decrypt_message(encrypted_message, num_columns, column_order):
    num_rows = len(encrypted_message) // num_columns

    # Create empty grid
    grid = [["" for _ in range(num_columns)] for _ in range(num_rows)]

    # Fill grid column-wise according to order
    idx = 0
    for col in column_order:
        col -= 1  # Convert 1-based index to 0-based
        for row in range(num_rows):
            grid[row][col] = encrypted_message[idx]
            idx += 1

    # Read rows to get decrypted message
    decrypted_message = "".join("".join(row) for row in grid)
    return decrypted_message

if __name__ == "__main__":
    print("Row-Column Transposition Cipher")

    message = input("Enter the message to be encrypted: ")
    num_columns = int(input("Enter the number of columns: "))
    
    column_order = list(map(int, input(f"Enter the column order (e.g., 3 1 4 2): ").split()))

    encrypted_message = encrypt_message(message, num_columns, column_order)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = decrypt_message(encrypted_message, num_columns, column_order)
    print(f"Decrypted message: {decrypted_message}")
