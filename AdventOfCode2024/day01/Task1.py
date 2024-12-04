leftNum = []
rightNum = []
difference = 0

with open('Dataset.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        numbers = line.split()
        leftNum.append(int(numbers[0]))
        rightNum.append(int(numbers[1]))
leftNum.sort()
rightNum.sort()
for idx, num in enumerate(leftNum):
    difference = difference + abs(num - rightNum[idx])

print("Diff: ", difference)
