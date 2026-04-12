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
    pass

def single_letter_grille_decrypt(cipherText: str) -> str:
    pass

def main():
    pass

if __name__ == "__main__":
    main()