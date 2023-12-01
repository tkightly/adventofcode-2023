"""https://adventofcode.com/2023/day/1"""
import re # regex module

WORDTODIGIT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open('1/input.txt', 'r', encoding="utf-8") as input_file:
    total = 0

    for row in input_file:

        row_int_array = []

        # match each digit and word within current row
        for match_group in re.finditer('(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))',\
row):
            digit = match_group.group(1)

            # if the current match is a word, replace it with a number
            # we are casting the ints as str, because we want += to concatenate them not add them 
            # together
            for word_to_replace in WORDTODIGIT:
                digit = digit.replace(word_to_replace, str(WORDTODIGIT[word_to_replace]))
            
            row_int_array.append(digit)

        row_calibration_value = ""
        row_calibration_value += str(row_int_array[0])
        row_calibration_value += str(row_int_array[-1])

        total += int(row_calibration_value)

    print(f"total is {total}")
input_file.close()
