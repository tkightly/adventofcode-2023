"""https://adventofcode.com/2023/day/1"""
import re

with open("1/input.txt", "r", encoding="utf-8") as input_file:
    total = 0

    for row in input_file:
        row_int_array = []
        row_calibration_value = ""

        for character in row:
            character = re.search("[0-9]", character)
            if character:
                row_int_array.append(int(character.group(0)))

        row_calibration_value += str(row_int_array[0])
        row_calibration_value += str(row_int_array[-1])

        total += int(row_calibration_value)
        print(
            f"ints are {row_int_array}, {row_int_array[0]} and {row_int_array[-1]} \
    equals {row_calibration_value}"
        )

    print(f"total is {total}")
input_file.close()
