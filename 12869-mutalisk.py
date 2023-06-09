n = int(input())
scv = list(map(int, input().split()))

if len(scv) < 3:
    scv += [0] * (3 - len(scv))

m = max(scv) + 1
r = [[[61 for _ in range(m)] for _ in range(m)]
     for _ in range(m)]

for i in range(0, scv[0] + 1):
    for j in range(scv[1] + 1):
        for k in range(scv[2] + 1):
            if i == j == k == 0:
                r[i][j][k] = 0
            else:
                r[i][j][k] = 1 + min(r[max(0, i - 9)][max(0, j - 3)][max(0, k - 1)],
                                     r[max(0, i - 9)][max(0, j - 1)][max(0, k - 3)],
                                     r[max(0, i - 3)][max(0, j - 9)][max(0, k - 1)],
                                     r[max(0, i - 3)][max(0, j - 1)][max(0, k - 9)],
                                     r[max(0, i - 1)][max(0, j - 9)][max(0, k - 3)],
                                     r[max(0, i - 1)][max(0, j - 3)][max(0, k - 9)])

print(r[scv[0]][scv[1]][scv[2]])
