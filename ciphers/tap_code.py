

TAP_MATRIX = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]
def find_position(letter):
    if letter == 'K':
        letter = 'C'

    row_number = 1

    for row in TAP_MATRIX:
        col_number = 1

        for char in row:
            if char == letter:
                return row_number, col_number
            col_number += 1

        row_number += 1

    return None
def encode_letter(letter):
    position = find_position(letter)

    if position is None:
        return ""

    row = position[0]
    col = position[1]

    taps_row = "." * row
    taps_col = "." * col

    return taps_row + " " + taps_col

def encrypt_tap_code(text):
    result = []
    text = text.strip().upper()

    for char in text:
        if char == " ":
            result.append("/")
        elif char.isalpha():
            code = encode_letter(char)
            if code != "":
                result.append(code)

    return "   ".join(result)

import code
import time

def visualize_tapcode_process(plainText):
    print("\n[VIZUALIZIMI I PROCESIT]\n")
    time.sleep(1)

    plainText = plainText.upper().strip()

    for char in plainText:
        if char == " ":
            print("/")
            time.sleep(1)
            print()
        elif char.isalpha():
            position = find_position(char)

            if position is not None:
                row = position[0]
                col = position[1]

                print(f"{char}:")

                print(" ".join(["."] * row))
                time.sleep(0.5)

                print(" ".join(["."] * col))
                time.sleep(1)

                print()

                def find_letter_by_position(row, col):
                    return TAP_MATRIX[row - 1][col - 1]
                
                def decode_letter(code):
                    parts = code.split()

                    if len(parts) != 2:
                        return ""

                    first_part = parts[0]
                    second_part = parts[1]

                    for char in first_part:
                        if char != ".":
                            return ""

                    for char in second_part:
                        if char != ".":
                            return ""

                    row = len(first_part)
                    col = len(second_part)

                    if row < 1 or row > 5:
                        return ""

                    if col < 1 or col > 5:
                        return ""

                    return find_letter_by_position(row, col)
                
                def decrypt_tap_code(cipher_text):
                    result = []

                    parts = cipher_text.split("   ")

                    for part in parts:
                        if part == "/":
                            result.append(" ")
                        else:
                            letter = decode_letter(part)
                            if letter != "":
                                result.append(letter)

                    return "".join(result)
                
                def visualize_tapcode_decryption(cipher_text):
                    print("\n[VIZUALIZIMI I DEKRIPTIMIT]\n")
                    time.sleep(1)

                    parts = cipher_text.split("   ")

                    for part in parts:
                        if part == "/":
                            print("/ -> hapesire")
                            time.sleep(1)
                            print()
                        else:
                            letter = decode_letter(part)

                            if letter != "":
                                print(f"{part} -> {letter}")
                                time.sleep(1)
                                print()
                
                    print(decode_letter(". ."))
                    print(decode_letter(".. ..."))
                    print(decode_letter("..... ....."))