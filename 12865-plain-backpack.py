n, k = map(int, input().split())

w = [0 for i in range(n + 1)]
v = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    w[i], v[i] = map(int, input().split())

r = [[0 for j in range(k + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if w[i] <= j:
            r[i][j] = max(r[i - 1][j], r[i - 1][j - w[i]] + v[i])
        else:
            r[i][j] = r[i - 1][j]

print(r[n][k])
