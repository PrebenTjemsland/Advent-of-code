

with open('testData.txt') as f:
    line_num = 0
    while True:
        line = f.readline().strip()
        line_num += 1
        if not line:
            break

