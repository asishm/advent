import re
import sys

def solve1(s):
    info = {}
    # print(s)
    for line in s.split('\n'):
        try:
            src, dests = re.search(r'(\d+) <-> (.*)', line).groups()
            dests = dests.split(', ')
            info[src] = dests
        except:
            print(repr(line))
    count = 0
    zero_count = 0
    keys = sorted((info.keys()))
    while keys:
        key = keys.pop()
        stack = info[key]
        visited = set([key])
        while stack:
            # print(len(stack))
            item = stack.pop()
            visited.add(item)
            to_add = list(set(info[item]) - visited)
            stack.extend(to_add)
        if '0' in visited:
            zero_count = len(visited)
        
        # print(count, len(keys), key, len(visited))
        count += 1
        keys = list(set(keys) - visited)
        # print(len(keys))
        # print('================')

    return zero_count, count

print(solve1("""0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""))

print(solve1(sys.stdin.read()))