import math
import re

sensors = []
beacons = []


def calculate_impossible_positions(sensor_y, dist, row):
    print(sensor_y, dist)
    overlap = 0
    if sensor_y + dist >= row >= sensor_y:
        overlap = sensor_y + dist - row
    if sensor_y - dist <= row < sensor_y:
        overlap = sensor_y - dist + row
    print(overlap)


data = [x.strip() for x in open('ExampleData.txt', 'r')]
for line in data:
    number_list = re.findall(r'\d+', line)
    sensor_x, sensor_y, beacon_x, beacon_y = list(map(int, number_list))
    dist = math.hypot(sensor_x - sensor_y, beacon_x - beacon_y)
    sensors.append([sensor_x, sensor_y, round(dist)])


test = sensors[6]
print(test)
calculate_impossible_positions(test[1], test[2], 10)

