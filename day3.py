# day 3

# part 1
from math import ceil
import itertools


def solve1(s):
    if s == 1:
        return 0
    max_sq = ceil(s ** 0.5)
    if max_sq % 2 == 0:
        max_sq += 1
    layer = max_sq // 2

    side_len = max_sq
    rem = abs((max_sq ** 2 - s) % (side_len - 1) - side_len // 2)

    return rem + layer


assert solve1(1) == 0
assert solve1(12) == 3
assert solve1(23) == 2
assert solve1(1024) == 31

print(solve1(368078))


def generate_dirs():
    directions = ['right', 'up', 'left', 'down']
    start = 1
    idx = 0
    while True:
        yield from itertools.repeat(directions[idx % 4], start)
        idx += 1
        yield from itertools.repeat(directions[idx % 4], start)
        idx += 1
        start += 1


class ExpandingGrid:

    dir_map = {
        'right': (0, 1),
        'left': (0, -1),
        'up': (-1, 0),
        'down': (1, 0)}

    def __init__(self, size=5):
        self.grid = [[0 for m in range(size)] for n in range(size)]
        self.size = size
        self.center = (size // 2, size // 2)
        self.set_val(self.center[0], self.center[1], 1)
        self.generator = generate_dirs()
        self.cur_coord = self.center

    def set_val(self, x, y, val):
        self.grid[x][y] = val

    def expand_grid(self):
        nsize = self.size * 2 + 1
        ngrid = [[0 for m in range(nsize)] for n in range(nsize)]
        translate = nsize // 2 - self.size // 2
        for i in range(self.size):
            for j in range(self.size):
                ngrid[i + translate][j + translate] = self.grid[i][j]
        self.grid = ngrid
        self.size = nsize
        self.center = (nsize // 2, nsize // 2)
        return translate

    def get_neighbor_sum(self, x, y, debug=False):
        total = 0
        for m in range(max(0, x - 1), min(x + 2, self.size)):
            for n in range(max(0, y - 1), min(y + 2, self.size)):
                if debug:
                    print(m, n, self.grid[m][n])
                total += self.grid[m][n]
        return total - self.grid[x][y]

    def get_next_coordinate(self):
        self.direction = next(self.generator)
        return self.cur_coord[0] + self.dir_map[self.direction][0], self.cur_coord[1] + self.dir_map[self.direction][1]

    def solve(self, n, debug=False):
        cur_val = 1
        while cur_val <= n:
            next_coord = self.get_next_coordinate()
            if debug:
                print(next_coord)
            for coord in next_coord:
                if coord < 0 or coord >= self.size:
                    translate = self.expand_grid()
                    next_coord = (next_coord[0] + translate, next_coord[1] + translate)
                    if debug:
                        print('expanding: next_coord: {}'.format(next_coord))
                    break
            cur_val = self.get_neighbor_sum(*next_coord)
            if debug:
                print(cur_val)
                print('=========')
                self.print_grid()
            self.set_val(*next_coord, cur_val)
            self.cur_coord = next_coord
        return cur_val

    def print_grid(self):
        for row in self.grid:
            print(' '.join(str(k) for k in row))


e = ExpandingGrid()
print(e.solve(368078, debug=False))