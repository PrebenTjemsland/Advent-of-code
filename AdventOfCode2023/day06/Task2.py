boat_speed = 0
boat_distance = 0
races = {}
times = []
distances = []
points = 1

with open('Dataset.txt') as f:
    line_num = 0
    while True:
        line = f.readline().strip()
        line_num += 1
        if not line:
            break
        number_string = line.split(":")[1:]
        numbers = number_string[0].split()
        number = ""
        for ele in numbers:
            number += ele
        if line_num == 1:
            time = int(number)
        if line_num == 2:
            distance = int(number)


time_held = 0
ways_to_win = 0
while time_held < time:
    current_distance = time_held * (time - time_held)
    if current_distance > distance:
        ways_to_win += 1
    time_held += 1
points *= ways_to_win

print(points)
