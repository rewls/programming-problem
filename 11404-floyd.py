n = int(input())
m = int(input())

r = [[1e5 + 1 for j in range(n + 1)] for i in range(n + 1)]

for k in range(m):
    i, j, w = map(int, input().split(" "))
    if r[i][j] > w:
        r[i][j] = w

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if j == k:
                r[j][k] = 0
            else:
                if r[j][k] > r[j][i] + r[i][k]:
                    r[j][k] = r[j][i] + r[i][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if r[i][j] == 1e5 + 1:
            print(0, end=" ")
        else:
            print(r[i][j], end=" ")
    print()
