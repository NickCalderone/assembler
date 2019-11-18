a_zero = ['0', '1', '-1', 'D', 'A', '!D', '!A', '-D', '-A', 'D+1', 'A+1', 'D-1', 'A-1', 'D+A', 'D-A', 'A-D', 'D&A',
          'D|A']
a_one = ['M', '!M', '-M', 'M+1', 'M-1', 'D+M', 'D-M', 'M-D', 'D&M', 'D|M']


def a_check(computation):
    if computation in a_zero:
        return '0'
    elif computation in a_one:
        return '1'
    else:
        return 'a_check error'
