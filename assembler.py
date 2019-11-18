from get_lines import get_lines
from ignore_comment import ignore_comment
from ignore_white import ignore_white
from ignore_blank_lines import ignore_blank_lines
from converter import converter

with open('nand2tetrisfiles/projects/06/max/MaxL.asm', 'r') as f:
    # clean up program lines
    full_program = get_lines(f)
    clean_program = ignore_comment(ignore_blank_lines(ignore_white(full_program)))
    # print(clean_program)

    # a operation/c operation handler
    value = converter(clean_program)
    print(value)
