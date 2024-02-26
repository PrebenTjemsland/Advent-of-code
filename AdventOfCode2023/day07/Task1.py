from collections import Counter
from collections import defaultdict

hands = {}


def find_dup_char(input):
    WC = Counter(input)
    output = {}
    for letter, count in WC.items():
        if count > 1:
            output.update({letter: count})
    return output


def sort_on_strength(x):
    print("sort on strength", x)
    strengths = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    if not a.isdigit() and b.isdigit():
        return True


def find_hand(hand):
    duplicates_unsorted = find_dup_char(hand)
    duplicates = sorted(duplicates_unsorted.items(), key=lambda x:x[1])
    ranks = ""
    for dup in duplicates:
        if dup[1] == 1:
            ranks += "7"
        if dup[1] == 2:
            ranks += "6"
        if dup[1] == 3:
            ranks += "4"
        if dup[1] == 4:
            ranks += "2"
        if dup[1] == 5:
            ranks += "1"
        ranks = ranks.replace("66", "5")
        ranks = ranks.replace("46", "3")
    return ranks


with open('testData.txt') as f:
    line_num = 0
    while True:
        line = f.readline().strip()
        line_num += 1
        if not line:
            break
        hand, bid = line.split()
        hands.update({hand: bid})
        hands = dict(sorted(hands.items()), )
hands_with_rank = {}
for hand in hands:
    hand_with_rank = find_hand(hand)
    hands_with_rank.update({hand: hand_with_rank})

#sorted(hands_with_rank.items(), lambda a,b:b[1]-a[1] or a[0]-b[0])
sorted(hands_with_rank.items(), key=lambda x: (-int(x[1]), sort_on_strength(x)))
