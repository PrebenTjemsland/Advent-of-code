mostCarriedCalories = 0
elfsCalories = 0

with open('Dataset.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line == '\n':
            if elfsCalories > mostCarriedCalories:
                mostCarriedCalories = elfsCalories
            elfsCalories = 0
        else: 
            calories = int(line)
            elfsCalories += calories
print(mostCarriedCalories)
