from ciphers.tap_code import encrypt_tap_code

text = input("Shkruaj tekstin: ")
encrypted_text = encrypt_tap_code(text)

print()
print("Teksti i enkriptuar:")
print(encrypted_text)
print()