from bin_c_line import bin_c_line


def no_jump(line):
    destination = line.split('=')[0]
    computation = line.split('=')[1]
    jump = 'null'
    return bin_c_line(computation, destination, jump)
