input1 = 272091
input2 = 815432


def same_adjacent_digits(num):
    num_list = [int(x) for x in str(num)]
    for i in range(5):
        if num_list[i] == num_list[i+1]:
            return True
    return False


def never_decrease(num):
    num_list = [int(x) for x in str(num)]
    for i in range(5):
        if num_list[i] > num_list[i + 1]:
            return False
    return True


def larger_group(num):
    num_list = [int(x) for x in str(num)]
    for i in range(5):
        if num_list[i] == num_list[i+1]:
            if i == 0 and num_list[0] != num_list[2]:
                return False
            elif i == 4 and num_list[4] != num_list[3]:
                return False
            elif num_list[i-1] != num_list[i] and num_list[i+1] != num_list[i+2]:
                return False
    return True


def password_count1(in1, in2):
    count = 0
    for psw in range(in1, in2+1):
        if len(str(psw)) != 6 or not same_adjacent_digits(psw) or not never_decrease(psw):
            continue
        count += 1
    return count


def password_count2(in1, in2):
    count = 0
    for psw in range(in1, in2+1):
        if len(str(psw)) != 6 or not never_decrease(psw) or larger_group(psw):
            continue
        count += 1
    return count


print(password_count1(input1, input2))
print(password_count2(input1, input2))
