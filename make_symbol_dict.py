def make_symbol_dict(lines):
    dictionary = {'R0': '0', 'R1': '1', 'R2': '2', 'R3': '3', 'R4': '4', 'R5': '5', 'R6': '6', 'R7': '7', 'R8': '8',
                  'R9': '9', 'R10': '10', 'R11': '11', 'R12': '12', 'R13': '13', 'R14': '14', 'R15': '15',
                  'SCREEN': '16384', 'KEYBOARD': '24576'}
    line_number = 0
    for l in lines:
        if l[0] == '(' and l[-1] == ')':
            key = l[1:-1]
            dictionary[key] = str(line_number)
        else:
            line_number += 1
    return dictionary
