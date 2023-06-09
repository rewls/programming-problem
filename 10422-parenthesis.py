t = int(input())

r = [0 for _ in range((int)(5000 / 2) + 1)]

def test(l):
    if l % 2 == 1:
        return 0
    m = (int)(l / 2)
    if r[m] > 0:
        return r[m]
    for i in range(1, m):
        r[m] += test(2 * i) * test(2 * (m - i))
    r[m] += 1
    return r[m]

for i in range(t):
    l = int(input())
    print(test(l) % (int)(1e9 + 7))
