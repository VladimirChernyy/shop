n = int(input())
matrix = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
        continue
for k in range(n):
    print(matrix[k])