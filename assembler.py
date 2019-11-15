from get_lines import get_lines
from ignore_comment import ignore_comment
from ignore_white import ignore_white


with open('nand2tetrisfiles/projects/06/add/Add.asm', 'r') as f:

    full_program = get_lines(f)
    clean_program = ignore_comment(list(filter(lambda a: a != "", ignore_white(full_program))))
    print(clean_program)



