def is_consistent(numbers, increasing=True):
    for i in range(len(numbers) - 1):
        if increasing:
            diff = numbers[i + 1] - numbers[i]
        else:
            diff = numbers[i] -numbers[i + 1]
        if diff > 3 or diff < 1:
            return False
    return True

safeCount = 0

with open('Dataset.txt') as f:
    for line in f:
        if line.strip():
            numbers = [int(num) for num in line.split()]
            if is_consistent(numbers, increasing=True) or is_consistent(numbers, increasing=False):
                safeCount += 1
                continue
            for i in range(len(numbers)):
                test_sequence = numbers[:i] + numbers[i + 1:]
                if is_consistent(test_sequence, increasing=True) or is_consistent(test_sequence, increasing=False):
                    safeCount += 1
                    break

print("The number of safe reports is:", safeCount)
