n = int(input())

b = [0 for i in range(n)]
r = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    b[i] = list(map(int, input().split()))

r[0][0] = 1
for i in range(n):
    for j in range(n):
        if b[i][j] == 0:
            continue
        i_next = i + b[i][j]
        j_next = j + b[i][j]
        if i_next >= n and j_next >= n:
            continue
        if i_next < n:
            r[i_next][j] += r[i][j]
        if j_next < n:
            r[i][j_next] += r[i][j]

print(r[n - 1][n - 1])
