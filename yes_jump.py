from bin_c_line import bin_c_line


def yes_jump(line):
    destination = 'null'
    computation = line.split(';')[0]
    jump = line.split(';')[1]
    return bin_c_line(computation, destination, jump)
