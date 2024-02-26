from collections import defaultdict

points = 0
winning_card = defaultdict(list)

with open('testData.txt') as f:
    line_num = 0
    while True:
        line = f.readline().strip()[10:]
        line_num += 1
        if not line:
            break
        winning_numbers_string, card_numbers_string = line.split("|")
        winning_numbers = winning_numbers_string.split()
        card_numbers = card_numbers_string.split()
        card_points = 0
        number_of_wins = 0
        for number in card_numbers:
            if number in winning_numbers:
                number_of_wins += 1
                card_copied = line_num+number_of_wins
                if not card_copied in winning_card:
                    winning_card[card_copied] = 1
                else:
                    winning_card[card_copied] += 1
print(winning_card)
print(sum(winning_card.values())
)
