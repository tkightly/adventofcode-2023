import re

input = open('1/input.txt', 'r')

total = 0

for row in input:

    row_int_array = []
    row_calibration_value = ""

    for character in row:
        character = re.search('[0-9]', character)
        if character:
            row_int_array.append(int(character.group(0)))

    row_calibration_value += str(row_int_array[0])
    row_calibration_value += str(row_int_array[-1])

    total += int(row_calibration_value)
    print(f"ints are {row_int_array}, {row_int_array[0]} and {row_int_array[-1]} equals {row_calibration_value}")

print(f"total is {total}")
input.close()