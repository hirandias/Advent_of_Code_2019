#Day 03
import time

with open('data.txt', 'r') as f:
    data = f.read().splitlines()

wire1 = data[0].split(',')
wire2 = data[1].split(',')


def gen_coordinates(wire):
    x, y = 0, 0
    coordinates = []
    for path in wire:

        # for _ in range(int(path[1:])):
        #     if path[0] == 'L':
        #         x -= 1
        #     elif path[0] == 'R':
        #         x += 1
        #     elif path[0] == 'U':
        #         y += 1
        #     elif path[0] == 'D':
        #         y -= 1
        #     coordinates.append((x, y))

        if path[0] == 'L':
            for i in range(int(path[1:])):
                x -= 1
                coordinates.append((x, y))

        elif path[0] == 'R':
            for i in range(int(path[1:])):
                x += 1
                coordinates.append((x, y))

        elif path[0] == 'U':
            for i in range(int(path[1:])):
                y += 1
                coordinates.append((x, y))

        elif path[0] == 'D':
            for i in range(int(path[1:])):
                y -= 1
                coordinates.append((x, y))

    return coordinates


# t1 = time.process_time()
wire1_coordinates = gen_coordinates(wire1)
wire2_coordinates = gen_coordinates(wire2)
# print(f'Performance test : {time.process_time() - t1}')

common = list(set(wire1_coordinates) & set(wire2_coordinates))

distance = [abs(x)+abs(y) for (x, y) in common]
print(min(distance))

steps = [wire1_coordinates.index(xy) + wire2_coordinates.index(xy) + 2 for xy in common]
print(min(steps))
