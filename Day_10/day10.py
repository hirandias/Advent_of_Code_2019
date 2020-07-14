#Day 10
import math
with open('data.txt', 'r') as f:
    data = f.read().splitlines()
asteroids_map = {(x, y): z for y, row in enumerate(data) for x, z in enumerate(row) if z == '#'}


def angle(x, y):
    return (math.atan2(x, y)+2*math.pi) % (2*math.pi)


angles_count = {xy1: len({angle(xy2[0] - xy1[0], xy2[1] - xy1[1]) for xy2 in asteroids_map if xy1 != xy2}) for xy1 in asteroids_map}
max_count = max(angles_count.values())
print(max_count)


def veporize_coordinates(a_map, station, num):
    distance_by_angle = {}
    for xy in a_map:
        if station != xy:
            dx, dy = xy[0] - station[0], station[1] - xy[1]
            distance_by_angle.setdefault(angle(dx, dy), []).append((dx**2+dy**2, xy))

    distance_by_angle = [(k, sorted(v)) for k, v in sorted(distance_by_angle.items())]
    count = 0
    while count != num:
        for item in distance_by_angle:
            if len(item[1]) > 0:
                nth_xy = item[1].pop(0)[1]
                count += 1
                if count == num:
                    break
    return nth_xy[0]*100 + nth_xy[1]


max_location = [k for k, v in angles_count.items() if v == max_count][0]
print(veporize_coordinates(asteroids_map, max_location, 200))
