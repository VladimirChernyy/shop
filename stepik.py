n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[n - i - 1][i] = 1
        if (i < j or i >= j) and i > n - 1 - j:
            matrix[i][j] = 2

for el in matrix:
    print(*el)
