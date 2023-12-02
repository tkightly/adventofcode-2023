"""https://adventofcode.com/2023/day/1"""
import re  # regex module

this_game_minimum_colours = {"red": 0, "green": 0, "blue": 0}
total = 0

with open("2/input.txt", "r", encoding="utf-8") as input_file:
    # print(input_file.read())
    for game in input_file:
        # Remove pesky line breaks
        game = game.strip()

        # Extract just the part of the game that relates to the colours and values for that set
        game = game.split(": ")

        # Then break each game into each set
        sets = game[1].split("; ")

        # reinitialise this game
        for COLOUR in this_game_minimum_colours:
            this_game_minimum_colours[COLOUR] = 0

        # For each set, loop through each COLOUR, then each draw to find the minimum needed value for that colour and save it to the this_game_minimum_colours dictionary
        for set in sets:
            draws = set.split(", ")
            for COLOUR in this_game_minimum_colours:
                for draw in draws:
                    # If the current draw is the colour we are interested in
                    if COLOUR == str(draw.split(" ")[1]):
                        # If the current draw is greater than any previously known values for this game, replace it
                        if int(draw.split(" ")[0]) > int(
                            this_game_minimum_colours[COLOUR]
                        ):
                            this_game_minimum_colours[COLOUR] = draw.split(" ")[0]

        # Multiply the values together to get the power of the set
        set_power = 1
        for colour in this_game_minimum_colours:
            set_power = set_power * int(this_game_minimum_colours[colour])

        # Add the power to the running total
        print(f"Set power for this game's minimum set is {set_power}")
        total += set_power

    print(f"Total is {total}")

input_file.close()
