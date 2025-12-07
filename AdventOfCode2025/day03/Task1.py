joltage = 0
with open('Dataset.txt') as f:
    line_num = 0
    while True:
        line = f.readline().strip()
        if not line:
            break
        line_num += 1
        lineNotLastNumber = line[:-1]
        index, val1 = max(enumerate(lineNotLastNumber), key=lambda x: (x[1].isdigit(), x[1]), default=(-1, None))
        lineAfterMax = line[index+1:]
        index, val2 = max(enumerate(lineAfterMax), key=lambda x: (x[1].isdigit(), x[1]), default=(-1, None))
        banksMax = str(val1) + str(val2)
        joltage = joltage + int(banksMax)


print("Joltage: ", joltage)
