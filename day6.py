# day 6

# part 1

from math import ceil
from collections import defaultdict

def getidxmax(s):
    return s.index(max(s))

def solve1(s, debug=False):
    seen = set()
    seen.add(tuple(s))

    steps = 0
    seen_idx = defaultdict(list)
    seen_idx[tuple(s)].append(0)

    while 1:
        i = getidxmax(s)
        val = s[i]
        dist = ceil(val / len(s))

        if debug:
            print(s)
            print(i, val)
            print(dist)
        
        n, rem = divmod(val, dist)


        s[i] = 0
        for j in range(i + 1, i + 1 + n):
            j = j % len(s)
            s[j] += dist
        s[(i + 1 + n) % len(s)] += rem

        steps += 1

        prev = len(seen)
        seen.add(tuple(s))
        seen_idx[tuple(s)].append(steps)

        if len(seen) == prev:
            return steps, seen_idx[tuple(s)][1] - seen_idx[tuple(s)][0] # part 1, part 2

def parse(s):
    return [int(k) for k in s.split()]

inp = '0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11'

assert solve1([0, 2, 7, 0], debug=True) == (5, 4)
print(solve1(parse(inp)))

# part 2
# see part 1