leftNum = []
rightNum = []
similarityScore = 0

with open('Dataset.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        numbers = line.split()
        leftNum.append(int(numbers[0]))
        rightNum.append(int(numbers[1]))

for num in leftNum:
    identicalNum = 0
    for num2 in rightNum:
        if num == num2:
            identicalNum += 1
    if identicalNum:
        similarityScore += num * identicalNum

print("Similarity score: ", similarityScore)
