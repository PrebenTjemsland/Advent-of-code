import math

with open('Dataset.txt') as f:
    lines = f.read().splitlines()

grid = []
for row in lines:
    grid.append(list(map(int, row)))
print(grid)
cols = list(zip(*grid))


def views(rowIndex,gridIndex):
    above = cols[rowIndex][:gridIndex]
    left = grid[gridIndex][:rowIndex]
    right = grid[gridIndex][rowIndex+1:]
    below = cols[rowIndex][gridIndex+1:]
    return [above[::-1], left[::-1], right, below]


p1 = 0
for gridIndex, row in enumerate(grid):
    for rowIndex, house in enumerate(row):
        if any(house > max(other or [-math.inf]) for other in views(rowIndex, gridIndex)):
            p1 += 1

print('p1',p1)

#p1 1662
#p2 537600
