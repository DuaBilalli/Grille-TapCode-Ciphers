from single_letter_grille import single_letter_grille_encrypt, single_letter_grille_decrypt, visualize_grille_process

def main():
    while True:
        print("\nZgjedhnni algoritmin që dëshironi të përdorni:\n")
        print("1. Single-Letter Grille")
        print("2. Tap Code")
        choice = input("\nZgjedh algoritmin që dëshironi të përdorni: ")

        if choice == "1":
            plainText = input("\nShkruaj plaintext-in: ")

            cipherText = single_letter_grille_encrypt(plainText)
            print(f"\nEncrypted:\n{cipherText}")

            decrypted = single_letter_grille_decrypt(cipherText)
            print(f"\nDecrypted: {plainText}")

            show = input("\nA dëshironi të shihni vizualizimin? (y/n): ").lower()
            if show == "y":
                visualize_grille_process(cipherText)

                
if __name__=="__main__":
    main()