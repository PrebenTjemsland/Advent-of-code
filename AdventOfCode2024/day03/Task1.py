import re

sum = 0
with open('Dataset.txt') as f:
    line_num = 0
    while True:
        line = f.readline().strip()
        line_num += 1
        if not line:
            break
        multipliers = re.findall(r'mul\(\d+,\d+\)', line)
        for multiply in multipliers:
            numbers = re.findall(r'\d+', multiply)
            [num1, num2] = numbers
            sum += int(num1) * int(num2)

print(sum)