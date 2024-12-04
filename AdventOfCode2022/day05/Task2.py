import re

initialStack1 = []
initialStack2 = []
initialStack3 = []
initialStack4 = []
initialStack5 = []
initialStack6 = []
initialStack7 = []
initialStack8 = []
initialStack9 = []

stacks_dict = {
        '1': initialStack1,
        '2': initialStack2,
        '3': initialStack3,
        '4': initialStack4,
        '5': initialStack5,
        '6': initialStack6,
        '7': initialStack7,
        '8': initialStack8,
        '9': initialStack9,
    }

with open('Dataset.txt') as data:
    data = data.readlines()
    stacks = [stack.strip('\n') for stack in data[:8]]
    instructions = [line.strip() for line in data[10:]]

    for crate in stacks:
        if crate[:4] != '    ':
            initialStack1.append(crate[1])
        if crate[4:8] != '    ':
            initialStack2.append(crate[5])
        if crate[8:12] != '    ':
            initialStack3.append(crate[9])
        if crate[12:16] != '   ':
            initialStack4.append(crate[13])
        if crate[16:20] != '   ':
            initialStack5.append(crate[17])
        if crate[12:16] != '   ':
            initialStack6.append(crate[21])
        if crate[16:20] != '   ':
            initialStack7.append(crate[25])
        if crate[20:24] != '   ':
            initialStack8.append(crate[29])
        if crate[24:27] != '  ':
            initialStack9.append(crate[33])

    for stack in stacks_dict.keys():
        stacks_dict[stack] = [crate for crate in stacks_dict[stack] if crate != ' ']

    for instruction in instructions:
        quanity, source, dest = re.findall(r'[0-9][0-9]*', instruction)
        move = stacks_dict[source][:int(quanity)]
        for operation in move:
            stacks_dict[source].remove(operation)
        stacks_dict[dest] = move + stacks_dict[dest]

    answer = ''
    for stack in stacks_dict.values():
        answer += stack[0]

    print(answer)
