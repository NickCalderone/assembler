from a_check import a_check
from bin_computation import bin_computation
from bin_destination import bin_destination
from bin_jump import bin_jump


def bin_c_line(computation, destination, jump):
    value = '111'
    operation = a_check(computation)
    value = value + operation + bin_computation(computation) + bin_destination(destination) + bin_jump(jump)
    return value
