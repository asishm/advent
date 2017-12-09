# day 9

# part 1

from collections import defaultdict

def solve1(s):
    parse = defaultdict(list)

    i = 0
    depth = 0
    total = 0
    in_garbage = False
    garbage_count = 0
    while i < len(s):
        if s[i] == '!':
            i += 2
            continue
        if in_garbage:
            if s[i] == '>':
                in_garbage = False
            else:
                garbage_count += 1
        elif s[i] == '<' and not in_garbage:
            in_garbage = True
        elif s[i] == '{':
            depth += 1
            total += depth
        elif s[i] == '}':
            depth -= 1
        i += 1
    return total, garbage_count

# assert solve1('{}') == 1
# assert solve1('{{{}}}') == 6
# assert solve1('{{},{}}') == 5
# assert solve1('{{{},{},{{}}}}') == 16
# assert solve1('{<a>,<a>,<a>,<a>}') == 1
# assert solve1('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
# assert solve1('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
# assert solve1('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3

print(solve1(input()))