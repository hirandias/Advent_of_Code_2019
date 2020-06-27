#Day 06

with open('data.txt', 'r') as f:
    data = {k: v for v, k in (a.split(')') for a in f.read().splitlines())}


def count_orbits(orbits):
    count = 0
    for value in orbits.values():
        while value != 'COM':
            value = orbits[value]
            count += 1
        count += 1
    return count


def orbits4obj(orbits, obj):
    obj_orbits = []
    value = orbits[obj]
    while value != 'COM':
        obj_orbits.append(value)
        value = orbits[value]

    return obj_orbits


print(count_orbits(data))
orbital_transfers = len(set(orbits4obj(data, 'YOU')) ^ set(orbits4obj(data, 'SAN')))
print(orbital_transfers)
