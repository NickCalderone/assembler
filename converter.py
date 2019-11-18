from a_operation import a_operation
from c_operation import c_operation


def converter(lines):
    bin_list = []

    for l in lines:
        if l[0] == '@':
            result = a_operation(l)
            bin_list.append(result)
        else:
            result = c_operation(l)
            bin_list.append(result)
    return bin_list
