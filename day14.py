# day 14

# part 1

data = 'nbysizxe'
rows = []
from day10 import solve
n = 0
for i in range(128):
    v = solve('%s-%d' % (data, i), byte=True)
    print(v)
    v = '{:0128b}'.format(int(v, 16))
    n += sum(map(int, v))
    rows.append(list(map(int, v)))

print(n)

seen = set()
n = 0
def dfs(i, j):
    if ((i, j)) in seen:
        return
    if not rows[i][j]:
        return
    seen.add((i, j))
    if i > 0:
        dfs(i-1, j)
    if j > 0:
        dfs(i, j-1)
    if i < 127:
        dfs(i+1, j)
    if j < 127:
        dfs(i, j+1)

for i in range(128):
    for j in range(128):
        if (i,j) in seen:
            continue
        if not rows[i][j]:
            continue
        n += 1
        dfs(i, j)

print(n)