dial = 50
numberOfZero = 0
range = 100

with open('Dataset.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        direction = line[0]
        numberOfMoves = int(line[1:])
        if direction == 'L':
            dial = (dial - numberOfMoves) % range
        if direction == 'R':
            dial = (dial + numberOfMoves) % range
        if dial == 0:
            numberOfZero += 1

print("Times at zero: ", numberOfZero)


