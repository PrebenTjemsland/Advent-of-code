import re

calibrationValue = 0

with open('Dataset.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        nums = ar = re.findall('[0-9]', line)
        print(nums)
        print(int(nums[0] + nums[-1]))
        calibrationValue += int(nums[0] + nums[-1])

print(calibrationValue)
