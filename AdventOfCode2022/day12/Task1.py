##Inspired by https://levelup.gitconnected.com/solve-a-maze-with-python-e9f0580979a1

maze = []
start = 0, 0
end = 2, 5

data = [x.strip() for x in open('ExampleData.txt', 'r')]
for line in data:
    maze.append(list(line))

matrix = []
for i in range(len(maze)):
    matrix.append([])
    for j in range(len(maze[i])):
        matrix[-1].append(0)
i, j = start
matrix[i][j] = 1


def make_step(k):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(chr(97 + k - 1))
            if matrix[i][j] == k:
                print(matrix)
                if i > 0 and matrix[i - 1][j] == 0 and maze[i - 1][j] == (chr(97 + k - 1)):
                    matrix[i - 1][j] = k + 1
                if j > 0 and matrix[i][j - 1] == 0 and maze[i][j - 1] == (chr(97 + k - 1)):
                    matrix[i][j-1] = k + 1
                if i < len(matrix) - 1 and matrix[i + 1][j] == 0 and maze[i + 1][j] == (chr(97 + k - 1)):
                    matrix[i+1][j] = k + 1
                if j < len(matrix[i]) - 1 and matrix[i][j + 1] == 0 and maze[i][j + 1] == (chr(97 + k - 1)):
                    matrix[i][j + 1] = k + 1


k = 0
old_matrix = []
while matrix[end[0]][end[1]] == 0:
    k += 1
    old_matrix = matrix
    make_step(k)
    ## Could break working code?
    if k > 10:
        break

i, j = end
k = matrix[i][j]
the_path = [(i,j)]
while k > 1:
    if i > 0 and matrix[i - 1][j] == k-1:
        i, j = i-1, j
        the_path.append((i, j))
        k-=1
    elif j > 0 and matrix[i][j - 1] == k-1:
        i, j = i, j-1
        the_path.append((i, j))
        k-=1
    elif i < len(matrix) - 1 and matrix[i + 1][j] == k-1:
        i, j = i+1, j
        the_path.append((i, j))
        k-=1
    elif j < len(matrix[i]) - 1 and matrix[i][j + 1] == k-1:
        i, j = i, j+1
        the_path.append((i, j))
        k -= 1
print(matrix)
