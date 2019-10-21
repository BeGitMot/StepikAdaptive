n, m = [int(x) for x in input().split()]
#n, m = 4, 4

field = ['.' for _ in range(n)]
for i in range(n):
    field[i] = []
    for j in input():
        field[i] += [j if j == '*' else 0]

#field = [[0, 0, '*', 0], ['*', '*', 0, 0], [0, 0, '*', 0], [0, 0, 0, 0]]

for i in range(n):
    for j in range(m):
        if field[i][j] != '*':
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if 0 <= (i + y) < n and 0 <= (j + x) < m:
                        field[i][j] = field[i][j] + (1 if field[i + y][j + x] == "*" else 0);

for i in range(n):
    print (*field[i], sep = '')

