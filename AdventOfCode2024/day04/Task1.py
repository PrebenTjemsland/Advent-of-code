def find_word(wordsearch, word):
    directions = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
    found_positions = []
    word_count = 0

    for i, row in enumerate(wordsearch):
        for j, c in enumerate(row):
            if c == word[0]:
                for direction in directions:
                    positions = check_dir(wordsearch, word, (i, j), direction)
                    if positions:
                        found_positions.append(positions)
                        word_count += 1

    if found_positions:
        for positions in found_positions:
            print_positions(wordsearch, positions)
        print(f'Word "{word}" found {word_count} times.')
    else:
        print('Word Not Found')


def check_dir(wordsearch, word, start_pos, direction):
    x, y = start_pos
    dx, dy = direction
    positions = []

    for char in word:
        if not (0 <= x < len(wordsearch) and 0 <= y < len(wordsearch[0])):
            return None
        if wordsearch[x][y] != char:
            return None
        positions.append((x, y))
        x += dx
        y += dy

    return positions


def print_positions(wordsearch, positions):
    for i, row in enumerate(wordsearch):
        line = "".join(f" {wordsearch[i][j]}" if (i, j) in positions else " -" for j in range(len(row)))
        print(line)
    print('')


wordsearch = open("Dataset.txt").read().splitlines()
find_word(wordsearch, 'XMAS')