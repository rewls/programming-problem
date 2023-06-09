def record(a, b, c, p1, p2):
    if a == 0 and b == 0 and c == 0:
        return True
    if a < 0 or b < 0 or c < 0:
        return False
    if v[a][b][c][p1][p2]:
        return False
    v[a][b][c][p1][p2] = True
    r[n - (a + b + c)] = 'A'
    if record(a - 1, b, c, 0, p1):
        return True
    if p1 != 1:
        r[n - (a + b + c)] = 'B'
        if record(a, b - 1, c, 1, p1):
            return True
    if p1 != 2 and p2 != 2:
        r[n - (a + b + c)] = 'C'
        if record(a, b, c - 1, 2, p1):
            return True
    return False

s = list(input())
n = len(s)
count = s.count('A'), s.count('B'), s.count('C')
r = ['' for i in range(n)]
v = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(n + 1)]
      for _ in range(n + 1)] for _ in range(n + 1)]
if record(*count, 0, 0):
    print(''.join(r))
else:
    print(-1)
