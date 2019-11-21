#!/usr/bin/env python3

import sys

from get_lines import get_lines
from ignore_comment import ignore_comment
from ignore_white import ignore_white
from ignore_blank_lines import ignore_blank_lines
from converter import converter 

file = sys.argv[1]

with open(f'/home/nick/PycharmProjects/coursera/nand2tetris/assembler/{file}', 'r') as f:
    # clean up program lines
    full_program = get_lines(f)
    clean_program = ignore_comment(ignore_blank_lines(ignore_white(full_program)))

    # a operation/c operation handler
    value = converter(clean_program)

    with open('result.hack', 'w') as r:
        for item in value:
            r.write("%s\n" % item)
