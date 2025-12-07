
invalidIdSum = 0

with open('Dataset.txt') as f:
    line = f.readline().strip()
    ranges = line.split(',')
    for range in ranges:
        rangeStart, rangeStop = range.split('-')
        currentId = int(rangeStart)
        while currentId <= int(rangeStop):
            left_text = str(currentId)[:len(str(currentId)) // 2].strip()
            right_text = str(currentId)[len(str(currentId)) // 2:].strip()
            if left_text == right_text:
                invalidIdSum += currentId
            currentId = currentId + 1


print("Sum: ", invalidIdSum)
