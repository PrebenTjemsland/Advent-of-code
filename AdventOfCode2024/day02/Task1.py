safe = 0

with open('Dataset.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        numbers = [int(num) for num in line.split()]
        isSafe = True
        increase = numbers[0] - numbers[1] < 0

        for idx, num in enumerate(numbers):
            if idx + 1 < len(numbers):
                if increase:
                    diff = numbers[idx + 1] - num
                else:
                    diff = num - numbers[idx + 1]
                if diff > 3 or diff < 1:
                    isSafe = False

        if  isSafe:
            safe += 1

print("Safe: ", safe)
