import re
from collections import defaultdict

engine_sum = 0
number_indices = {}
symbol_indices = {}
valid_symbols = "!@#$%^&*()_-+={}[]"
hits = defaultdict(list)

with open('testData.txt') as f:
    line_num = 0
    while True:
        line = f.readline().strip()
        line_num += 1
        if not line:
            break
        number_index = [i for i in range(0, len(line)) if line[i].isdigit()]
        number_indices.update({line_num: number_index})
        symbol_index = [i for i in range(0, len(line)) if line[i] in valid_symbols]
        symbol_indices.update({line_num: symbol_index})

with open('testData.txt') as f:
    line_num = 0
    for index, numbers in enumerate(number_indices.values()):
        for number in numbers:
            if number + 1 in symbol_indices[index + 1]:
                hits[index + 1].append(number)
            if number - 1 in symbol_indices[index + 1]:
                hits[index - 1].append(number)

    while True:
        line = f.readline().strip()
        line_num += 1
        if not line:
            break
        if line_num in hits:
            for num_index in hits[line_num]:
                print("after: ", line[:num_index])
                print("before: ", line[num_index:])
                print("line number: ", line_num, "after",  re.findall(r"^\d+", line[:num_index]))
                print("line number: ", line_num, "before: ", re.findall(r"(\d+)\D", line[num_index:]))


print(engine_sum)


#467..114..
#...*......


