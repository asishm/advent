import sys
import time

def parse(s):
    s = s.strip().split('\n')
    max_layer = int(s[-1].split(': ')[0].strip()) + 1
    # print(max_layer)
    states = [None] * max_layer
    depths = [None] * max_layer
    dirs = [None] * max_layer

    for item in s:
        layer, depth = [int(k) for k in item.split(": ")]  
        # print(layer, depth)
        depths[layer] = depth
        val = layer % (depth * 2 - 2)
        if val > depth - 1:
            val = 2 * (depth - 1) - val
        states[layer] = val
        dirs[layer] = 1


    def calculate_state_at_layer(t, layer, depths):
        depth = depths[layer]
        if depth is None:
            return
        val = t % (depth * 2 - 2)
        if val > depth - 1:
            return 2 * (depth - 1) - val
        return val

    def calculate_state(delay, depths):
        times = (delay + i for i in range(len(depths)))
        state = all(filter(lambda x: x is not None, (calculate_state_at_layer(t, i, depths) for (t, i) in zip(times, range(len(depths))))))
        # print(delay, state)
        return state

    start = time.time()
    delay = 0
    while True:
        state = calculate_state(delay, depths)
        if state:
            print(time.time() - start)
            return delay
        delay += 1
        if delay % 100000 == 0:
            print('delay:', delay, '==========')

print(parse("""0: 3
1: 2
4: 4
6: 4"""))

print(parse(sys.stdin.read()))     