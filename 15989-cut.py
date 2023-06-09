T = int(input())

n = []
for i in range(T):
    n.append(int(input()))

r = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 1]]

for i in range(T):
    if n[i] < len(r):
        print(sum(r[n[i]]))
        continue
    k = len(r)
    while k <= n[i]:
        r.append([0, 0, 0])
        r[k][2] = sum(r[k - 3])
        r[k][1] = sum(r[k - 2][:2])
        r[k][0] = r[k - 1][0]
        k += 1
    print(sum(r[n[i]]))
