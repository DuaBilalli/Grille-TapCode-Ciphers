import string
import random

def grille_positions() -> list:
    #pozitat per vrimat e lira
    return [
        (0,1), (1,4), (2,2),
        (2,3), (3,0), (3,2),
        (4,5), (5,1), (5,3)
    ]

def random_char() -> chr:
    return random.choice(string.ascii_uppercase + string.digits)

def single_letter_grille_encrypt(plainText: str) -> str:
    holes = grille_positions()

    plainText = plainText.replace(" ", "").upper()
    index = 0
    cipherText = ""

    while index < len(plainText):
        grid = {}

        #i mbush holes me plaintext
        for (i,j) in holes:
            if index < len(plainText):
                grid[(i,j)] = plainText[index]
                index += 1
            else:
                grid[(i,j)] = 'X'

        #i mbush pjeset tjera me random characters
        for i in range(6):
            for j in range(6):
                if (i,j) not in grid:
                    grid[(i,j)] = random_char()

        #krijon ciphertextin nga grid
        for i in range(6):
            for j in range(6):
                cipherText += grid[(i,j)]

    #newline cdo 36 karaktere
    formattedCipherText = ""
    for i in range(0, len(cipherText), 36):
        formattedCipherText += cipherText[i:i+36] + "\n"

    return formattedCipherText

def single_letter_grille_decrypt(cipherText: str) -> str:
    holes = grille_positions()

    cipherText = cipherText.replace("\n", "")
    block_size = 36

    plainText = ""

    for b in range(0, len(cipherText), block_size):
        block = cipherText[b:b+block_size]

        grid = {}
        k = 0

        for i in range(6):
            for j in range(6):
                grid[(i,j)] = block[k]
                k += 1

        for (i,j) in holes:
            plainText += grid[(i,j)]

    return plainText.rstrip('X')

def main():
    text = input("Shkruaj tekstin: ")

    encrypted = single_letter_grille_encrypt(text)
    print(f"\nEncrypted:\n{encrypted}")

    decrypted = single_letter_grille_decrypt(encrypted)
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()