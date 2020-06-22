#Day 01
import functools

with open('data.txt', 'r') as f:
    masses = [int(x) for x in f.read().splitlines()]


def calculate_fuel(mass):
    return int(mass/3)-2


print(functools.reduce(lambda acc, mass: acc + calculate_fuel(mass), masses, 0))


def include_fuel4fuel(mass):
    tot_fuel = fuel = calculate_fuel(mass)

    while fuel > 8:
        fuel = calculate_fuel(fuel)
        tot_fuel += fuel

    return tot_fuel


print(functools.reduce(lambda acc, mass: acc+include_fuel4fuel(mass), masses, 0))
