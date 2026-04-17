

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

