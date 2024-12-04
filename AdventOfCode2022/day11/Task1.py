import math


monkeys = {
    "monkey 0": [56, 56, 92, 65, 71, 61, 79],
    "monkey 1": [61, 85],
    "monkey 2": [54, 96, 82, 78, 69],
    "monkey 3": [57, 59, 65, 95],
    "monkey 4": [62, 67, 80],
    "monkey 5": [91],
    "monkey 6": [79, 83, 64, 52, 77, 56, 63, 92],
    "monkey 7": [50, 97, 76, 96, 80, 56]
}
current_monkey = ""
worries = {}
test = False
monkey_operations = {
    "monkey 0": 0,
    "monkey 1": 0,
    "monkey 2": 0,
    "monkey 3": 0,
    "monkey 4": 0,
    "monkey 5": 0,
    "monkey 6": 0,
    "monkey 7": 0,
}
i = 0
while i < 20:
    i += 1
    data = [x.strip() for x in open('Dataset.txt', 'r')]
    for line_with_case in data:
        line = line_with_case.lower()
        if "monkey" in line:
            current_monkey = line.strip(":")
        if "operation" in line:
            split_line = line.split(" ")
            for item in monkeys[current_monkey]:
                monkey_operations[current_monkey] += 1
                if "old" in str(split_line[5]):
                    split_line[5] = item
                if "*" in split_line[4]:
                    inspection_worry = int(item) * int(split_line[5])
                    worries[item] = math.floor(inspection_worry / 3)
                if "+" in split_line[4]:
                    inspection_worry = int(item) + int(split_line[5])
                    worries[item] = math.floor(inspection_worry / 3)
                if "-" in split_line[4]:
                    inspection_worry = int(item) - int(split_line[5])
                    worries[item] = math.floor(inspection_worry / 3)
        if "test" in line:
            split_line = line.split(" ")
            for worry in worries:
                if worry % int(split_line[3]) == 0:
                    test = True
                if "if true" in line and test == True:
                    text, monkey = line.split(" throw to ")
                    monkeys[monkey].append(worry)
                if "if false" in line and test == False:
                    text, monkey = line.split(" throw to ")
                    monkeys[monkey].append(worry)

monkey_operations_sorted = dict(sorted(monkey_operations.items(), key=lambda item: item[1], reverse=True))
most_active_monkeys = {monkey_operations_sorted[key] for key in list(monkey_operations_sorted)[:2]}

print(math.prod(most_active_monkeys))

#24696 to low

#67830 correct
