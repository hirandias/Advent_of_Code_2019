# day 07
import itertools

with open('data.txt', 'r') as f:
    data = [int(x) for x in f.read().split(',')]


class Amplifier:
    def __init__(self, program, phase_setting):
        self.program = program
        self.length = len(program)
        self.program[self.program[1]] = phase_setting
        self.output = None
        self.input_value = None
        self.halt = False
        self.key = 2

    def get_output(self, input_value):
        self.input_value = input_value
        self.execute_program()
        return self.output

    def execute_program(self):
        while self.key < self.length:
            if self.program[self.key] == 99:
                self.halt = True
                break

            elif self.program[self.key] == 1:
                self.program[self.program[self.key+3]] = self.program[self.program[self.key+1]] + self.program[self.program[self.key+2]]
                self.key += 4
            elif self.program[self.key] == 101:
                self.program[self.program[self.key + 3]] = self.program[self.key + 1] + self.program[self.program[self.key + 2]]
                self.key += 4
            elif self.program[self.key] == 1001:
                self.program[self.program[self.key + 3]] = self.program[self.program[self.key + 1]] + self.program[self.key + 2]
                self.key += 4
            elif self.program[self.key] == 1101:
                self.program[self.program[self.key + 3]] = self.program[self.key + 1] + self.program[self.key + 2]
                self.key += 4

            elif self.program[self.key] == 2:
                self.program[self.program[self.key+3]] = self.program[self.program[self.key+1]] * self.program[self.program[self.key+2]]
                self.key += 4
            elif self.program[self.key] == 102:
                self.program[self.program[self.key+3]] = self.program[self.key+1] * self.program[self.program[self.key+2]]
                self.key += 4
            elif self.program[self.key] == 1002:
                self.program[self.program[self.key + 3]] = self.program[self.program[self.key + 1]] * self.program[self.key + 2]
                self.key += 4
            elif self.program[self.key] == 1102:
                self.program[self.program[self.key+3]] = self.program[self.key+1] * self.program[self.key+2]
                self.key += 4

            elif self.program[self.key] == 3:
                self.program[self.program[self.key+1]] = self.input_value
                self.key += 2

            elif self.program[self.key] == 4:
                self.output = self.program[self.program[self.key+1]]
                self.key += 2
                break
            elif self.program[self.key] == 104:
                self.output = self.program[self.key+1]
                self.key += 2
                break

            elif self.program[self.key] == 5:
                self.key = self.program[self.program[self.key+2]] if self.program[self.program[self.key+1]] != 0 else self.key + 3
            elif self.program[self.key] == 105:
                self.key = self.program[self.program[self.key+2]] if self.program[self.key+1] != 0 else self.key + 3
            elif self.program[self.key] == 1005:
                self.key = self.program[self.key+2] if self.program[self.program[self.key+1]] != 0 else self.key + 3
            elif self.program[self.key] == 1105:
                self.key = self.program[self.key+2] if self.program[self.key+1] != 0 else self.key + 3

            elif self.program[self.key] == 6:
                self.key = self.program[self.program[self.key+2]] if self.program[self.program[self.key+1]] == 0 else self.key + 3
            elif self.program[self.key] == 106:
                self.key = self.program[self.program[self.key+2]] if self.program[self.key+1] == 0 else self.key + 3
            elif self.program[self.key] == 1006:
                self.key = self.program[self.key+2] if self.program[self.program[self.key+1]] == 0 else self.key + 3
            elif self.program[self.key] == 1106:
                self.key = self.program[self.key+2] if self.program[self.key+1] == 0 else self.key + 3

            elif self.program[self.key] == 7:
                self.program[self.program[self.key+3]] = 1 if self.program[self.program[self.key+1]] < self.program[self.program[self.key+2]] else 0
                self.key += 4
            elif self.program[self.key] == 107:
                self.program[self.program[self.key+3]] = 1 if self.program[self.key+1] < self.program[self.program[self.key+2]] else 0
                self.key += 4
            elif self.program[self.key] == 1007:
                self.program[self.program[self.key+3]] = 1 if self.program[self.program[self.key+1]] < self.program[self.key+2] else 0
                self.key += 4
            elif self.program[self.key] == 1107:
                self.program[self.program[self.key+3]] = 1 if self.program[self.key+1] < self.program[self.key+2] else 0
                self.key += 4

            elif self.program[self.key] == 8:
                self.program[self.program[self.key+3]] = 1 if self.program[self.program[self.key+1]] == self.program[self.program[self.key+2]] else 0
                self.key += 4
            elif self.program[self.key] == 108:
                self.program[self.program[self.key+3]] = 1 if self.program[self.key+1] == self.program[self.program[self.key+2]] else 0
                self.key += 4
            elif self.program[self.key] == 1008:
                self.program[self.program[self.key+3]] = 1 if self.program[self.program[self.key+1]] == self.program[self.key+2] else 0
                self.key += 4
            elif self.program[self.key] == 1108:
                self.program[self.program[self.key+3]] = 1 if self.program[self.key+1] == self.program[self.key+2] else 0
                self.key += 4

            else:
                return f'Intcode program error @ Key:{self.key} - Value: {self.program[self.key]}'


def amp_maxout(ps1, ps2):
    max_output = 0
    for perm in itertools.permutations([p for p in range(ps1, ps2)]):
        amplifiers = [Amplifier(data.copy(), phase) for phase in perm]

        output = 0
        while not amplifiers[0].halt:
            for a in amplifiers:
                output = a.get_output(output)

        max_output = output if output > max_output else max_output

    return max_output


print(amp_maxout(0, 5))
print(amp_maxout(5, 10))
