#Day 09
with open('data.txt', 'r') as f:
    data = [int(x) for x in f.read().split(',')]

boost = {key: value for key, value in enumerate(data)}


class Initcode():

    def __init__(self, program):
        self.prog = program
        self.key = 0
        self.input_value = None
        self.output = None
        self.relative_base = 0

    def execute(self, input_val):
        self.input_value = input_val

        def get_key(k, mode):
            if mode == '0':
                opr_key = self.prog[k]
            elif mode == '1':
                opr_key = k
            elif mode == '2':
                opr_key = self.prog[k] + self.relative_base
            return opr_key

        def addition(operands):
            opr1_key = get_key(self.key+1, operands[2])
            opr2_key = get_key(self.key+2, operands[1])
            opr3_key = get_key(self.key+3, operands[0])
            self.prog[opr3_key] = self.prog.get(opr1_key, '0') + self.prog.get(opr2_key, '0')
            self.key += 4

        def multiplication(operands):
            opr1_key = get_key(self.key+1, operands[2])
            opr2_key = get_key(self.key+2, operands[1])
            opr3_key = get_key(self.key+3, operands[0])
            self.prog[opr3_key] = self.prog.get(opr1_key, 0) * self.prog.get(opr2_key, 0)
            self.key += 4

        def set_input(operands):
            opr1_key = get_key(self.key+1, operands[2])
            self.prog[opr1_key] = self.input_value
            self.key += 2

        def set_output(operands):
            opr1_key = get_key(self.key+1, operands[2])
            self.output = self.prog[opr1_key]
            self.key += 2

        def jump_1(operands):
            opr1_key = get_key(self.key + 1, operands[2])
            opr2_key = get_key(self.key + 2, operands[1])
            self.key = self.prog[opr2_key] if self.prog[opr1_key] != 0 else self.key+3

        def jump_2(operands):
            opr1_key = get_key(self.key + 1, operands[2])
            opr2_key = get_key(self.key + 2, operands[1])
            self.key = self.prog[opr2_key] if self.prog[opr1_key] == 0 else self.key+3

        def greater_to(operands):
            opr1_key = get_key(self.key+1, operands[2])
            opr2_key = get_key(self.key+2, operands[1])
            opr3_key = get_key(self.key+3, operands[0])
            self.prog[opr3_key] = 1 if self.prog.get(opr1_key, 0) < self.prog.get(opr2_key, 0) else 0
            self.key += 4

        def equal_to(operands):
            opr1_key = get_key(self.key+1, operands[2])
            opr2_key = get_key(self.key+2, operands[1])
            opr3_key = get_key(self.key+3, operands[0])
            self.prog[opr3_key] = 1 if self.prog.get(opr1_key, 0) == self.prog.get(opr2_key, 0) else 0
            self.key += 4

        def set_relative_base(operands):
            opr1_key = get_key(self.key+1, operands[2])
            self.relative_base += self.prog[opr1_key]
            self.key += 2

        while self.prog[self.key] != 99:
            ropcode = str(self.prog[self.key]).zfill(2)[-2:]
            lopcode = str(self.prog[self.key]).zfill(5)[0:3]

            if ropcode == '01':
                addition(lopcode)
            elif ropcode == '02':
                multiplication(lopcode)
            elif ropcode == '03':
                set_input(lopcode)
            elif ropcode == '04':
                set_output(lopcode)
            elif ropcode == '05':
                jump_1(lopcode)
            elif ropcode == '06':
                jump_2(lopcode)
            elif ropcode == '07':
                greater_to(lopcode)
            elif ropcode == '08':
                equal_to(lopcode)
            elif ropcode == '09':
                set_relative_base(lopcode)
        return self.output


compute1 = Initcode(boost.copy())
compute2 = Initcode(boost.copy())
print(compute1.execute(1))
print(compute2.execute(2))
