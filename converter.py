from a_operation import a_operation
from o_operation import o_operation


def converter(lines):
    bin_list = []

    for l in lines:
        if l[0] == '@':
            result = a_operation(l)
            bin_list.append(result)
        else:
            result = o_operation(l)
            bin_list.append(result)
