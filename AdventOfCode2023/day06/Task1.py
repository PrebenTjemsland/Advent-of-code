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
        numbers = res = [int(ele) for ele in number_string[0].split()]
        if line_num == 1:
            times = numbers
        if line_num == 2:
            distances = numbers


for idx, time in enumerate(times):
    time_held = 0
    ways_to_win = 0
    while time_held < time:
        distance = time_held * (time - time_held)
        if distance > distances[idx]:
            ways_to_win += 1
        time_held += 1
    points *= ways_to_win

print(points)
