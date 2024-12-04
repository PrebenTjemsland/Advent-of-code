signal_strength = 0
x_register = 1
cycles = 1

line_one = []
line_two = []
line_three = []
line_four = []
line_five = []
line_six = []


def add_drawing(cycle):
    if cycle <= 40:
        print(cycle, x_register)
        if x_register -1 <= cycle <= x_register +1:
            line_one.insert(cycle, "#")
        else:
            line_one.insert(cycle, ".")
    elif cycle <= 80:
        if x_register -1 <= cycle - 40 <= x_register +1:
            line_two.insert(cycle, "#")
        else:
            line_two.insert(cycle, ".")
    elif cycle <= 120:
        if x_register -1 <= cycle - 80 <= x_register +1:
            line_three.insert(cycle, "#")
        else:
            line_three.insert(cycle, ".")
    elif cycle <= 160:
        if x_register -1 <= cycle - 120 <= x_register +1:
            line_four.insert(cycle, "#")
        else:
            line_four.insert(cycle, ".")
    elif cycle <= 200:
        if x_register -1 <= cycle - 160 <= x_register +1:
            line_five.insert(cycle, "#")
        else:
            line_five.insert(cycle, ".")
    elif cycle <= 240:
        if x_register -1 <= cycle - 200 <= x_register +1:
            line_six.insert(cycle, "#")
        else:
            line_six.insert(cycle, ".")


data = [x.strip() for x in open('ExampleData.txt', 'r')]
for line in data:
    if cycles > 240:
        break
    if cycles == 20:
        signal_strength += (cycles * x_register)
    elif (cycles - 20) % 40 == 0:
        signal_strength += (cycles * x_register)
    if line == "noop":
        cycles += 1
        pass
    add_drawing(cycles)
    if line != "noop":
        command, number = line.split(" ")
        cycles += 1
        if cycles > 240:
            break
        add_drawing(cycles)
        if cycles == 20:
            signal_strength += (cycles * x_register)
        elif (cycles - 20) % 40 == 0:
            signal_strength += (cycles * x_register)
        cycles += 1
        x_register += int(number)

print(line_one)
print(line_two)
print(line_three)
print(line_four)
print(line_five)
print(line_six)

