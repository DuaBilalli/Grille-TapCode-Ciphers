import string

def grille_positions() -> list:
    #pozitat per vrimat e lira
    return [
        (0,1), (1,4), (2,2),
        (2,3), (3,0), (3,2),
        (4,5), (5,1), (5,3)
    ]
def single_letter_grille_encrypt(plainText: str) -> str:
    pass

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