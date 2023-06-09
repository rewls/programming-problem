n = int(input())
c = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split(" "))
    c[u].append(v)
    c[v].append(u)

r = [[0, 1] for _ in range(n + 1)]
v = [False for _ in range(n + 1)]

def dfs(i):
    v[i] = True
    for j in c[i]:
        if v[j] == False:
            dfs(j)
            r[i][0] += r[j][1]
            r[i][1] += min(r[j][0], r[j][1])

dfs(1)
print(min(r[1][0], r[1][1]))
