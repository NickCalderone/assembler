from get_lines import get_lines
from ignore_comment import ignore_comment
from ignore_white import ignore_white
from ignore_blank_lines import ignore_blank_lines

with open('nand2tetrisfiles/projects/06/max/MaxL.asm', 'r') as f:

    full_program = get_lines(f)
    clean_program = ignore_comment(ignore_blank_lines(ignore_white(full_program)))
    print(clean_program)
