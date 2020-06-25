# Day 05

with open('data.txt', 'r') as f:
    data = [int(x) for x in f.read().split(',')]


def execute_program(program, input_value):
    key = 0
    output = None

    while program[key] != 99:

        if program[key] == 1:
            program[program[key+3]] = program[program[key+1]] + program[program[key+2]]
            key += 4
        elif program[key] == 101:
            program[program[key + 3]] = program[key + 1] + program[program[key + 2]]
            key += 4
        elif program[key] == 1001:
            program[program[key + 3]] = program[program[key + 1]] + program[key + 2]
            key += 4
        elif program[key] == 1101:
            program[program[key + 3]] = program[key + 1] + program[key + 2]
            key += 4

        elif program[key] == 2:
            program[program[key+3]] = program[program[key+1]] * program[program[key+2]]
            key += 4
        elif program[key] == 102:
            program[program[key+3]] = program[key+1] * program[program[key+2]]
            key += 4
        elif program[key] == 1002:
            program[program[key + 3]] = program[program[key + 1]] * program[key + 2]
            key += 4
        elif program[key] == 1102:
            program[program[key+3]] = program[key+1] * program[key+2]
            key += 4

        elif program[key] == 3:
            program[program[key+1]] = input_value
            key += 2

        elif program[key] == 4:
            output = program[program[key+1]]
            key += 2
        elif program[key] == 104:
            output = program[key+1]
            key += 2

        elif program[key] == 5:
            key = program[program[key+2]] if program[program[key+1]] != 0 else key + 3
        elif program[key] == 105:
            key = program[program[key+2]] if program[key+1] != 0 else key + 3
        elif program[key] == 1005:
            key = program[key+2] if program[program[key+1]] != 0 else key + 3
        elif program[key] == 1105:
            key = program[key+2] if program[key+1] != 0 else key + 3

        elif program[key] == 6:
            key = program[program[key+2]] if program[program[key+1]] == 0 else key + 3
        elif program[key] == 106:
            key = program[program[key+2]] if program[key+1] == 0 else key + 3
        elif program[key] == 1006:
            key = program[key+2] if program[program[key+1]] == 0 else key + 3
        elif program[key] == 1106:
            key = program[key+2] if program[key+1] == 0 else key + 3

        elif program[key] == 7:
            program[program[key+3]] = 1 if program[program[key+1]] < program[program[key+2]] else 0
            key += 4
        elif program[key] == 107:
            program[program[key+3]] = 1 if program[key+1] < program[program[key+2]] else 0
            key += 4
        elif program[key] == 1007:
            program[program[key+3]] = 1 if program[program[key+1]] < program[key+2] else 0
            key += 4
        elif program[key] == 1107:
            program[program[key+3]] = 1 if program[key+1] < program[key+2] else 0
            key += 4

        elif program[key] == 8:
            program[program[key+3]] = 1 if program[program[key+1]] == program[program[key+2]] else 0
            key += 4
        elif program[key] == 108:
            program[program[key+3]] = 1 if program[key+1] == program[program[key+2]] else 0
            key += 4
        elif program[key] == 1008:
            program[program[key+3]] = 1 if program[program[key+1]] == program[key+2] else 0
            key += 4
        elif program[key] == 1108:
            program[program[key+3]] = 1 if program[key+1] == program[key+2] else 0
            key += 4

        else:
            return f'Intcode program error @ Key:{key} - Value: {program[key]}'

    return output


print(execute_program(data.copy(), 1))
print(execute_program(data.copy(), 5))
