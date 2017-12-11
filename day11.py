# day 11

# part 1

def solve1(s):
    maps = {
        'n': (0, 2),
        'ne': (1, 1),
        'e': (2, 0),
        'se': (1, -1),
        's': (0, -2),
        'sw': (-1, -1),
        'w': (-2, 0),
        'nw': (-1, 1)
    }

    x, y = 0, 0
    furth = 0
    for ins in s:
        chgx, chgy = maps[ins]
        x += chgx
        y += chgy
        tmpx, tmpy = abs(x), abs(y)
        min_ = min(tmpx, tmpy)
        rem = (tmpx + tmpy - 2 * min_) // 2
        furth = max(furth, min_ + rem)
    x, y = abs(x), abs(y)
    print(x, y)
    min_ = min(x, y)
    rem = (x + y - 2 * min_) // 2
    return min_ + rem, furth

def parse(s):
    return [k for k in s.split(',')]


# assert solve1(parse('ne,ne,ne')) == 3
# assert solve1(parse('ne,ne,sw,sw')) == 0
# assert solve1(parse('ne,ne,s,s')) == 2
# assert solve1(parse('se,sw,se,sw,sw')) == 3
print(solve1(parse(input())))