# day 15

import time

def solve(astart, bstart, count, gen_func, part='1'):
    start = time.time()
    afac, bfac, mod = 16807, 48271, 2147483647
    amul, bmul = (4, 8) if part == '2' else (1, 1)
    agen = gen_func(astart, afac, mod, amul)
    bgen = gen_func(bstart, bfac, mod, bmul)
    c = 0
    comp = 2 ** 16
    for _ in range(count):
        # if _ % (count // 10) == 0:
        #     print(_)
        aval = next(agen)
        bval = next(bgen)
        if not (aval - bval) % comp: # % comp replace with & 0xffff
            c += 1
            #print(_)
    print(time.time() - start)
    return c

# solve(65, 8921)

def gen(start, fac, mod, mul, *args):
    while True:
        start = (start * fac) % mod
        if start % mul == 0:
            yield start

print(solve(116, 299, 40000000, gen))
print(solve(116, 299, 5000000, gen, '2'))
# print(solve2(116, 299)