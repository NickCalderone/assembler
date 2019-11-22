from get_lines import get_lines
from ignore_comment import ignore_comment
from ignore_white import ignore_white
from ignore_blank_lines import ignore_blank_lines
from get_lines import get_lines


def parser(file):
    full_program = get_lines(file)
    clean_program = ignore_comment(ignore_blank_lines(ignore_white(full_program)))
    return clean_program
