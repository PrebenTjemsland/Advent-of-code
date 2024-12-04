from functools import partial
import math

with open('Dataset.txt') as f:
    lines = f.read().splitlines()

grid = []
for y, row in enumerate(lines):
    grid.append(list(map(int,row)))

cols = list(zip(*grid))


def views(rowIndex,gridIndex):
    above = cols[rowIndex][:gridIndex]
    left = grid[gridIndex][:rowIndex]
    right = grid[gridIndex][rowIndex+1:]
    below = cols[rowIndex][gridIndex+1:]
    return [above[::-1], left[::-1], right, below]


def direction_score(house, direction):

    t = 0
    for num in direction:
        t += 1
        if num >= house:
            break
    return t


p2 = 0
for gridIndex, row in enumerate(grid):
    for rowIndex, house in enumerate(row):
        dir_score = partial(direction_score, house)
        score = math.prod(map(dir_score, views(rowIndex,gridIndex)))
        if score > p2:
            p2 = score

print('p2',p2)