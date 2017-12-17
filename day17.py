# day 17

def solve1(s, n):
    inp = [0]
    cur_pos = 0
    for k in range(1, n + 1):
        if k % 50_000 == 0:
            print(k)
        cur_pos = (cur_pos + s) % len(inp)
        inp.insert(cur_pos + 1, k)
        #print(inp)
        cur_pos += 1
    if n == 2107:
        return inp[inp.index(2017) + 1]
    return inp[inp.index(0) + 1]

print(solve1(3, 2017))

def solve2(s, n):
    len_inp = 1
    cur_pos = 0
    beside0 = None
    for k in range(1, n+1):
        if k % 1_000_000 == 0:
            print(k)
        cur_pos = (cur_pos + s) % len_inp + 1
        if cur_pos == 1:
            beside0 = k
        len_inp += 1
    return beside0
print(solve2(344, 50_000_000))