rules = []
instructions = []
correct_instructions_sum = 0

with open('Dataset.txt') as f:
    line_num = 0
    rules_done = False
    while True:
        line = f.readline().strip()
        line_num += 1
        if not line and not rules_done:
            rules_done = True
        elif not line and rules_done:
            break
        if not rules_done:
            key, value = map(int, line.split('|'))
            rules.append((key, value))
        elif rules_done and line:
            instructions.append([int(num) for num in line.split(',')])

new_instructions = []

for instruction in instructions:
    should_remove = False
    for rule in rules:
        first, second = rule
        if first in instruction and second in instruction:
            first_index = instruction.index(first)
            second_index = instruction.index(second)
            if second_index < first_index:
                should_remove = True
                break
    if not should_remove:
        new_instructions.append(instruction)

instructions = new_instructions

for instruction in new_instructions:
    mid_num = instruction[len(instruction) // 2]
    correct_instructions_sum += mid_num
print("sum: ", correct_instructions_sum)
