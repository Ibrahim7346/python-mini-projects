def caeser_cipher(text, shift):
    encrypted_text =  ""

    for char in text:
        if char.isalpha(): #check if it is a letter
            shift_base = ord('A') if char.isupper() else ord('a')

            encrypted_char = chr(
                (ord(char) - shift_base + shift) % 26 + shift_base
            )

            encrypted_text += encrypted_char
        else:
            encrypted_text += char    # keep spaces and symbols unchanged

    return encrypted_text

message = input("Enter a message: ")
shift = int(input("Enter shift value: "))

encrypted = caeser_cipher(message, shift)

print("Encrypted message:", encrypted)