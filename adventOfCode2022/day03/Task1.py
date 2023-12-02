from curses.ascii import isupper

point = 0
data = [x.strip() for x in open('Dataset.txt', 'r')]
for line in data:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    for letter in firstpart:
        if letter in secondpart:
            if isupper(letter):
                point += ord(letter) - 38
                break
            point += ord(letter) - 96
            break
print(point)
