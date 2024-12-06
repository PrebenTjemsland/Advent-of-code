import copy

rules = []
instructions = []
correct_instructions_sum = 0
not_correct = True
fixed_instructions = []

with open('TestData.txt') as f:
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


def fix_instructions(instructions, first_run):
    fixed_instructions.clear()
    fixed = False
    for instruction in instructions:
        for rule in rules:
            first, second = rule
            if first in instruction and second in instruction:
                first_index = instruction.index(first)
                second_index = instruction.index(second)
                if second_index < first_index:
                    instruction[first_index], instruction[second_index] = instruction[second_index], instruction[first_index]
                    fixed = True
                    break
        if fixed or not first_run:
            fixed_instructions.append(instruction)


def check_instruction(instructions):
    for instruction in instructions:
        for rule in rules:
            first, second = rule
            if first in instruction and second in instruction:
                first_index = instruction.index(first)
                second_index = instruction.index(second)
                if second_index < first_index:
                    return True
    return False

first_run = True
while not_correct:
    fix_instructions(instructions, first_run)
    instructions = copy.deepcopy(fixed_instructions)
    not_correct = check_instruction(instructions)
    first_run = False

for instruction in fixed_instructions:
    mid_num = instruction[len(instruction) // 2]
    correct_instructions_sum += mid_num
print("sum: ", correct_instructions_sum)






#11428 too high
#possebli ducplicates

# Initialize variables
rules = []
instructions = []
correct_instructions_sum = 0
not_correct = True
to_be_fixed_instructions = []

# Read the input file
with open('Dataset.txt') as f:
    rules_done = False
    for line in f:
        line = line.strip()
        if not rules_done:
            if not line:
                rules_done = True
            else:
                key, value = map(int, line.split('|'))
                rules.append((key, value))
        elif line:
            instructions.append([int(num) for num in line.split(',')])

print("Rules:", rules)
print("Instructions:", instructions)

# Check if instruction needs fixing
def check_instruction(instruction):
    for rule in rules:
        first, second = rule
        if first in instruction and second in instruction:
            first_index = instruction.index(first)
            second_index = instruction.index(second)
            if second_index < first_index:
                return True
    return False

# Fix instruction according to rules
def fix_instruction(instruction):
    fixed = instruction.copy()
    changed = True
    while changed:
        changed = False
        for rule in rules:
            first, second = rule
            if first in fixed and second in fixed:
                first_index = fixed.index(first)
                second_index = fixed.index(second)
                if second_index < first_index:
                    fixed[first_index], fixed[second_index] = fixed[second_index], fixed[first_index]
                    changed = True
    return fixed

# Main script to process instructions
for instruction in instructions:
    if check_instruction(instruction):
        fixed_instruction = fix_instruction(instruction)
        to_be_fixed_instructions.append(fixed_instruction)

# Calculate sum of middle values
for instruction in to_be_fixed_instructions:
    mid_num = instruction[len(instruction) // 2]
    correct_instructions_sum += mid_num

print("Sum: ", correct_instructions_sum) # Expected output: 123