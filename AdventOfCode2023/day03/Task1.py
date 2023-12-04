import re

engine_sum = 0
number_indices = {}
symbol_indices = {}
valid_symbols = "!@#$%^&*()_-+={}[]"


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

print(number_indices)
print(symbol_indices)
print(engine_sum)


#467..114..
#...*......