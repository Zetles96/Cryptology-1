def encrypt(plain_text: str, shift: int) -> str:
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                shift_char = chr((ord(char) + shift - 65) % 26 + 65)
            else:
                shift_char = chr((ord(char) + shift - 97) % 26 + 97)
            cipher_text += shift_char
        else:
            cipher_text += char
    return cipher_text


def decrypt(cipher_text: str, shift: int) -> str:
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            if char.isupper():
                shift_char = chr((ord(char) - shift - 65) % 26 + 65)
            else:
                shift_char = chr((ord(char) - shift - 97) % 26 + 97)
            plain_text += shift_char
        else:
            plain_text += char
    return plain_text


if __name__ == '__main__':
    text = "Hello World!"
    shift = 10
    encrypted_text = encrypt(plain_text=text, shift=shift)
    print(encrypted_text)
    print(encrypt(encrypted_text, shift=26 - shift))
    print(decrypt(encrypted_text, shift=shift))
