
import math

with open('data.txt', 'r') as f:
    masses = [int(x) for x in f.read().splitlines()]

def calculate_fuel(mass):
    return math.floor(mass/3)-2


tot_fuel = 0
fuel_4_masses = 0
for mass in masses:
    fuel_4_module = fuel_4_fuel = calculate_fuel(mass)
    fuel_4_masses += fuel_4_module

    while fuel_4_fuel > 8:
        fuel_4_fuel = calculate_fuel(fuel_4_fuel)
        fuel_4_module += fuel_4_fuel

    tot_fuel += fuel_4_module

print(fuel_4_masses)
print(tot_fuel)
