from itertools import pairwise
from dataclasses import dataclass

with open('Dataset.txt') as f:
    txt = f.read()

lines = txt.split('\n')

tail_pos = set()
tail_pos.add((0, 0))

@dataclass
class Knot:
    x : int
    y : int
    tail : bool

# choose number of knots (only difference between part1 & part2) here
knot_count = 10 # part1: 2, part2: 10

rope = [Knot(0, 0, i == knot_count-1) for i in range(knot_count)]

def check_knots(knot1 : Knot, knot2 : Knot):
    if abs(knot1.x - knot2.x) == 2:  # right or left
        knot2.x += 1 if knot2.x < knot1.x else -1
        # check diagonal movement: up or down.
        # part 1 lets you get away with just assigning knot2's y to equal knot1's y
        # but there are edge cases of diagonal interpolating on long ropes
        # where an assignment changes knot2's y by 2 when it should be only 1.
        if knot2.y < knot1.y:
            knot2.y += 1
        elif knot1.y < knot2.y:
            knot2.y -= 1
    elif abs(knot1.y - knot2.y) == 2:    # up or down
        knot2.y += 1 if knot2.y < knot1.y else -1
        # check left or right.
        if knot2.x < knot1.x:
            knot2.x += 1
        elif knot1.x < knot2.x:
            knot2.x -= 1
    else:
        return

    if knot2.tail:
        tail_pos.add((knot2.x, knot2.y))

for l in lines:
    move, amount = l.split(' ')

    for i in range(int(amount)):
        match move:
            case 'R':
                rope[0].x += 1
            case 'L':
                rope[0].x -= 1
            case 'U':
                rope[0].y += 1
            case 'D':
                rope[0].y -= 1

        for knot1,knot2 in pairwise(rope):
            check_knots(knot1, knot2)

print(len(tail_pos))