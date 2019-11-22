#!/usr/bin/env python3
import sys
from parser import parser
from code import code

in_file = sys.argv[1]
out_file = sys.argv[2]

with open(f'/home/nick/PycharmProjects/coursera/nand2tetris/assembler/{in_file}', 'r') as f:
    clean_program = parser(f)
    value = code(clean_program)

    with open(f'{out_file}', 'w') as r:
        for item in value:
            r.write("%s\n" % item)
