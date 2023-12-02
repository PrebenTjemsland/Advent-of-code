from curses.ascii import isupper

point = 0
firstElf = ""
secondElf = ""
i = 0
x = 3
data = [x.strip() for x in open('Dataset.txt', 'r')]

while x <= len(data):
    group = data[i:i + 3]
    for letter in group[0]:
        if letter in group[1]:
            if letter in group[2]:
                if isupper(letter):
                    point += ord(letter) - 38
                    i += 3
                    break
                point += ord(letter) - 96
                i += 3
                break
print(point)
