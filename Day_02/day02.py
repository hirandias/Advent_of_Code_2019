#Day 02

with open('data.txt', 'r') as f:
    data = [int(x) for x in f.read().split(',')]


def execute_program(program, noun, verb):
    program[1], program[2] = noun, verb
    opcode_key = 0

    while program[opcode_key] != 99:
        if program[opcode_key] == 1:
            program[program[opcode_key+3]] = program[program[opcode_key+1]] + program[program[opcode_key+2]]
        elif program[opcode_key] == 2:
            program[program[opcode_key+3]] = program[program[opcode_key+1]] * program[program[opcode_key+2]]
        else:
            return 'Intcode Program Error!'

        opcode_key += 4

    return program[0]


print(execute_program(data.copy(), 12, 2))


def find_inputs(program, output):

    for noun in range(100):
        for verb in range(100):
            if execute_program(program.copy(), noun, verb) == output:
                return noun*100 + verb

    return f'No match found for {output}'


print(find_inputs(data, 19690720))
