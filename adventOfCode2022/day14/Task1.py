import math

cave_walls = {}
rounded_coordinate = []

def views(row_index,grid_index):
    above = cols[row_index][:grid_index]
    left = grid[grid_index][:row_index]
    right = grid[grid_index][row_index+1:]
    below = cols[row_index][grid_index+1:]
    return [above[::-1], left[::-1], right, below]


data = [x.strip() for x in open('ExampleText.txt', 'r')]
for line in data:
    grid = []
    coordinates = list(line.replace(",", ".").split(" -> "))
    for coordinate in coordinates:
        rounded_coordinate.append(round(float(coordinate)))
    grid.append(rounded_coordinate)


cols = list(zip(*grid))

p1 = 0
for gridIndex, row in enumerate(grid):
    for rowIndex, house in enumerate(row):
        if any(house > max(other or [-math.inf]) for other in views(rowIndex, gridIndex)):
            p1 += 1

print(grid)
