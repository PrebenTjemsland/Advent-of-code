import re

sum = 0
with open('Dataset.txt') as f:
    content = f.read()
    content = content.replace('\n', '')
    pattern = r"don\'t\(\).*?do\(\)"
    trimmedString = re.sub(pattern, '', content)
    print(trimmedString)
    multipliers = re.findall(r'mul\(\d+,\d+\)', trimmedString)
    for multiply in multipliers:
        numbers = re.findall(r'\d+', multiply)
        [num1, num2] = numbers
        sum += int(num1) * int(num2)
print(sum)

