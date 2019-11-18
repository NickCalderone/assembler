from no_jump import no_jump
from yes_jump import yes_jump


def c_operation(line):
    if line.find('=') >= 0:
        result = no_jump(line)
        return result
    elif line.find(';') >= 0:
        result = yes_jump(line)
        return result
    else:
        print('error: didnt find ; or = in program')