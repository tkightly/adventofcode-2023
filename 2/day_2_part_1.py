"""https://adventofcode.com/2023/day/1"""
import re  # regex module

RULES = ["12 red", "13 green", "14 blue"]
total = 0

with open("2/input.txt", "r", encoding="utf-8") as input_file:
    # print(input_file.read())
    for game in input_file:
        rule_violated = False
        game = game.split(": ")
        game_id = game[0]
        sets = game[1].split("; ")
        # print(game_id)

        for set in sets:
            # print(set)
            draws = set.split(", ")

            for draw in draws:
                # print(draw)
                for RULE in RULES:
                    if int(RULE.split(" ")[0]) < int(draw.split(" ")[0]) and str(
                        RULE.split(" ")[1]
                    ) == str(draw.split(" ")[1]):
                        # print(RULE.split(" ")[0])
                        # print(draw.split(" ")[0])
                        print(f"{game_id}: draw '{draw}' would violate rule '{RULE}'")
                        rule_violated = True

        if rule_violated == False:
            total += int(game_id.split(" ")[1])

    print(f"Total is {total}")

input_file.close()
