def ignore_blank_lines(lines):
    value = list(filter(lambda x: x != "", lines))
    return value
