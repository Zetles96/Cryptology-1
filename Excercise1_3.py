def decrypt(cipher_text: str, shift: int) -> str:
    plain_text = ""
    for char in cipher_text:
        shift_char = chr((ord(char) - shift) % 127)
        plain_text += shift_char

    return plain_text


def decrypt_all(cipher_text: str) -> None:
    for i in range(127):
        decrypted = decrypt(cipher_text, i)
        print(f"{i}:\t{decrypted}")


if __name__ == '__main__':
    text = ";\\r6TXfTe~r[bjrTeXrlbhrWb\\aZ2rHf\\aZrUeb^XarVelcgb~r[h[2r;TccXafrgbrg[XrUXfgrbYrhf!!!rAXkgrg\`XrTebhaW~rgelr48F $%+r\\ar:T_b\\fr6bhagXer@bWXsss"
    decrypt_all(text)
    print(decrypt(text, 114))
