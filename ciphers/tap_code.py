

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
            result.append(code)

    return "   ".join(result)

