points = 0

with open('Dataset.txt') as f:
    line_num = 0
    while True:
        line = f.readline().strip()[10:]
        line_num += 1
        if not line:
            break
        winning_numbers_string, card_numbers_string = line.split("|")
        winning_numbers = winning_numbers_string.split()
        card_numbers = card_numbers_string.split()
        number_of_wins = 0
        card_points = 0
        for number in card_numbers:
            if number in winning_numbers:
                card_points = 1 * 2 ** number_of_wins
                number_of_wins += 1

        points += card_points
print(points)
