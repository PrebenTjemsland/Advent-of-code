count = 0

def getNumbers(sections):
    firstSector, lastSector = sections.split("-")
    return [int(firstSector), int(lastSector)]

data = [x.strip() for x in open('Dataset.txt', 'r')]
for line in data:
    firstpart, secondpart = line.split(",")
    firstSectors = getNumbers(firstpart)
    secondSectors = getNumbers(secondpart)
    if secondSectors[0] <= firstSectors[0] <= secondSectors[1]:
        count += 1
    elif secondSectors[0] <= firstSectors[1] <= secondSectors[1]:
        count += 1
    elif firstSectors[0] <= secondSectors[0] <= firstSectors[1]:
        count += 1
    elif firstSectors[0] <= secondSectors[1] <= firstSectors[1]:
        count += 1

print(count)


