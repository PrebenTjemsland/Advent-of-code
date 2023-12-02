import re

sum_of_power = 0
bagContains = {"red": 12, "green": 13, "blue": 14}


def get_game_id(line):
    start = 'Game '
    end = ':'
    return line[line.find(start) + len(start):line.rfind(end)]


def is_game_set_possible(game_set):
    red = game_set.split(" red")[0][-2:]
    green = game_set.split(" green")[0][-2:]
    blue = game_set.split(" blue")[0][-2:]
    if not red.strip().isdigit():
        red = 0
    if not blue.strip().isdigit():
        blue = 0
    if not green.strip().isdigit():
        green = 0
    return int(red), int(blue), int(green)


with open('Dataset.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        red = 0
        blue = 0
        green = 0
        stripped_line = line.rstrip()
        game_possible = True
        game_ID = get_game_id(stripped_line)
        game_sets = stripped_line.split(";")
        for game_set in game_sets:
            new_red, new_blue, new_green = is_game_set_possible(game_set)
            if red < new_red:
                red = new_red
            if green < new_green:
                green = new_green
            if blue < new_blue:
                blue = new_blue
        sum_of_power += blue * red * green

print("result: ", sum_of_power)