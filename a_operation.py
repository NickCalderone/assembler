def a_operation(line):
    number = bin(int(line[1:]))[2:]
    bin_number = str(number).zfill(16)
    return bin_number
