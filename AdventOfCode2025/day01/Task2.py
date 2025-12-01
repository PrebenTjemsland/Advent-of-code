dial = 50
numberOfZero = 0
range = 100
totalWraps = 0

with open('Dataset.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        direction = line[0]
        numberOfMoves = int(line[1:])
        if direction == 'L':
            temp_val = dial - numberOfMoves
            wraps = abs(temp_val // range)
            totalWraps += wraps
            dial = temp_val % range

        elif direction == 'R':
            temp_val = dial + numberOfMoves
            wraps = temp_val // range
            totalWraps += wraps
            dial = temp_val % range

numberOfZero = numberOfZero + totalWraps

print("Times at zero: ", numberOfZero)