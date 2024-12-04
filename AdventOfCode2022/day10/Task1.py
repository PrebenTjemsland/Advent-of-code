signal_strength = 0
x_register = 1
cycles = 1

data = [x.strip() for x in open('Dataset.txt', 'r')]
for line in data:
    if cycles > 220:
        break
    if cycles == 20:
        signal_strength += (cycles * x_register)
    elif (cycles - 20) % 40 == 0:
        signal_strength += (cycles * x_register)
    if line == "noop":
        cycles += 1
        pass
    if line != "noop":
        command, number = line.split(" ")
        cycles += 1
        if cycles > 220:
            break
        if cycles == 20:
            signal_strength += (cycles * x_register)
        elif (cycles - 20) % 40 == 0:
            signal_strength += (cycles * x_register)
        cycles += 1
        x_register += int(number)

print(signal_strength)
