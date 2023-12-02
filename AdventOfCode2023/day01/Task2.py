import regex as re
calibrationValue = 0


def w2n(number):
    matches = re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', number, overlapped=True)
    lookup = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    if matches[0].isdigit():
        first = matches[0]
    else:
        first = lookup[matches[0]]
    if matches[-1].isdigit():
        last = matches[-1]
    else:
        last = lookup[matches[-1]]
    return int(first + last)


with open('Dataset.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        calibrationValue += w2n(line)


print(calibrationValue)
