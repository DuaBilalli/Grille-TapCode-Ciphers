

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