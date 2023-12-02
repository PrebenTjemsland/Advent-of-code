sum_of_ids = 0
bagContains = {"red": 12, "green": 13, "blue": 14}


def get_game_id(line):
    start = 'Game '
    end = ':'
    return line[line.find(start) + len(start):line.rfind(end)]


def is_game_set_possible(game_set):
    red = game_set.split(" red")[0][-2:]
    green = game_set.split(" green")[0][-2:]
    blue = game_set.split(" blue")[0][-2:]
    if red.strip().isdigit():
        red_possible = int(red) <= bagContains["red"]
    else:
        red_possible = True
    if blue.strip().isdigit():
        blue_possible = int(blue) <= bagContains["blue"]
    else:
        blue_possible = True
    if green.strip().isdigit():
        green_possible = int(green) <= bagContains["green"]
    else:
        green_possible = True
    if red_possible and blue_possible and green_possible:
        return True
    return False


with open('Dataset.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        stripped_line = line.rstrip()
        game_possible = True
        game_ID = get_game_id(stripped_line)
        game_sets = stripped_line.split(";")
        for game_set in game_sets:
            if not is_game_set_possible(game_set):
                game_possible = False
        if game_possible:
            sum_of_ids += int(game_ID)

print("result: ", sum_of_ids)
