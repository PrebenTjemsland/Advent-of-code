import numpy as np

x_mas_pattern = np.array([
    ['M', '.', 'S'],
    ['.', 'A', '.'],
    ['M', '.', 'S']
])
x_mas_pattern_2 = np.array([
    ['M', '.', 'M'],
    ['.', 'A', '.'],
    ['S', '.', 'S']
])

x_mas_pattern_3 = np.array([
    ['S', '.', 'S'],
    ['.', 'A', '.'],
    ['M', '.', 'M']
])

x_mas_pattern_4 = np.array([
    ['S', '.', 'M'],
    ['.', 'A', '.'],
    ['S', '.', 'M']
])


def matches_pattern(data, pattern):
    count = 0
    rows, cols = data.shape
    p_rows, p_cols = pattern.shape
    for i in range(rows - p_rows + 1):
        for j in range(cols - p_cols + 1):
            sub_array = data[i:i + p_rows, j:j + p_cols]
            if np.all((pattern == '.') | (sub_array == pattern)):
                count +=1
                print(f"Pattern found at position: ({i}, {j})")
    return count


with open('Dataset.txt', 'r') as file:
    data = file.read().splitlines()
data_array = np.array([list(line) for line in data])
num = 0
num += matches_pattern(data_array, x_mas_pattern)
num += matches_pattern(data_array, x_mas_pattern_2)
num += matches_pattern(data_array, x_mas_pattern_3)
num += matches_pattern(data_array, x_mas_pattern_4)
print("total: ", num)