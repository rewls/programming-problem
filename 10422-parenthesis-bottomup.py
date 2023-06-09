t = int(input())

max = (int)(5e3) // 2 + 1
r = [0 for _ in range(max)]

r[0] = 1
for i in range(1, max):
    for j in range(1, i + 1):
        r[i] += r[j - 1] * r[i - j]
    r[i] %= (int)(1e9 + 7)

for i in range(t):
    l = int(input())
    if l % 2 == 1:
        print(0)
    else:
        print(r[l // 2])
