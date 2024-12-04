folders = {}
data = [x.strip() for x in open('ExampleData.txt', 'r')]
folder = ""
totalSize = 0
dictionaryStructure = {}


def get_structure():
    current_dict = ""
    for command in data:
        command_split = command.split(" ")
        if command_split[1] == "cd" and command_split[2] != "..":
            dictionaryStructure[command_split[2]] = current_dict
            current_dict = command_split[2]
        if command_split[1] == "cd" and command_split[2] == "..":
            current_dict = dictionaryStructure.get(current_dict)


for line in data:
    size = 0
    splitLine = line.split(" ")

    try:
        size = int(splitLine[0])
    except ValueError:
        pass
    if splitLine[1] == "cd" and splitLine[2] != "..":
        folder = splitLine[2]
        folders[splitLine[2]] = 0
    if size > 0:
        folders[folder] += size

#Add folders to each other


get_structure()


sortedResult = (dict(sorted(folders.items(), key=lambda item: item[1], reverse=True)))
for key, value in sortedResult.items():
    if value >= 100000:
        continue
    totalSize += value
print(totalSize)

# 1325879 too low
