from single_letter_grille import single_letter_grille_encrypt, single_letter_grille_decrypt, visualize_grille_process
from tap_code import encrypt_tap_code, decrypt_tap_code, visualize_tapcode_process, visualize_tapcode_decryption

def main():
    while True:
        print("\nZgjedhnni algoritmin që dëshironi të përdorni:\n")
        print("1. Single-Letter Grille")
        print("2. Tap Code")
        print("3. Dil")

        choice = input("\nZgjedhja: ")

        if choice == "1":

            print("\n1. Encrypt")
            print("2. Decrypt")

            grille_choice = input("\nZgjedh veprimin: ")

            if grille_choice == "1":
                plainText = input("\nShkruaj plaintext-in: ")
                cipherText = single_letter_grille_encrypt(plainText)
                print(f"\nEncrypted:\n{cipherText}")

                show = input("A dëshironi të shihni vizualizimin? (y/n): ").lower()
                if show == "y":
                    visualize_grille_process(cipherText)

            elif grille_choice == "2":
                cipherText = input("\nShkruaj ciphertext-in: ")

                if len(cipherText) % 36 != 0:
                    print("\nCiphertext nuk është valid.")
                else:
                    plainText = single_letter_grille_decrypt(cipherText)
                    print(f"Decrypted:\n{plainText}")

                    show = input("A dëshironi të shihni vizualizimin? (y/n): ").lower()
                    if show == "y":
                        visualize_grille_process(cipherText)

            else:
                print("\nZgjedhje e pavlefshme.")

        elif choice == "2":
            print("\n1. Encrypt")
            print("2. Decrypt")

            tap_choice = input("\nZgjedh veprimin: ")

            if tap_choice == "1":
                plainText = input("\nShkruaj plaintext-in: ")

                cipherText = encrypt_tap_code(plainText)
                print(f"\nEncrypted:\n{cipherText}")

                show = input("\nA dëshironi të shihni vizualizimin? (y/n): ").lower()
                if show == "y":
                    visualize_tapcode_process(plainText)

            elif tap_choice == "2":
                cipherText = input("\nShkruaj tap code-in: ")

                decryptedText = decrypt_tap_code(cipherText)
                print()
                print("Decrypted:")
                print(decryptedText)
                print()

                show = input("\nA dëshironi të shihni vizualizimin? (y/n): ").lower()
                if show == "y":
                    visualize_tapcode_decryption(cipherText)

            else:
                print("\nZgjedhje e pavlefshme.")

        elif choice == "3":
            print("\nProgrami u mbyll me sukses. Faleminderit!")
            break

        else:
            print("\nZgjedhje e pavlefshme! Provoni përsëri!")

if __name__ == "__main__":
    main()