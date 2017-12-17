# day 16
import sys


def parse(s):
    return [(k[0], k[1:].split('/')) for k in s.strip().split(',')]

def rot(s, k):
    k = k % len(s)
    return s[-k:] + s[:-k]

def solve1(s, n=16, niter=1_000_000_000):
    pats = [chr(ord('a') + k) for k in range(n)]
    pos = {k:i for i,k in enumerate(pats)}
    # print(s)
    seen, n_bef, period = [], None, None
    for _ in range(niter):
        if _ % 100_000_000 == 0:
            print(_)
        for ins, oth in s:
            if ins == 's':
                oth = int(oth[0])
                pats = rot(pats, oth)
                pos = {k:i for i,k in enumerate(pats)}
            elif ins == 'x':
                # print(oth)
                a, b = [int(k) for k in oth]
                sa, sb = pats[a], pats[b]
                pos[sa], pos[sb] = b, a
                pats[b], pats[a] = sa, sb
            elif ins == 'p':
                a, b = oth
                posa, posb = pos[a], pos[b]
                pos[a], pos[b] = posb, posa
                pats[posb], pats[posa] = a, b
        prev = len(seen)
        to_add = "".join(pats)
        if to_add in seen:
            n_bef = seen.index(to_add)
            period = _ - n_bef
            to_ret = 1_000_000_000 % period
            break
        seen.append(to_add)
        
    return ''.join(pats), n_bef, period, seen, seen[to_ret - 1] if period else None

# print(solve1(parse("""s1,x3/4,pe/b"""), 5))
s = parse(sys.stdin.read())
print(solve1(s, niter=1))
rets = print(solve1(s))