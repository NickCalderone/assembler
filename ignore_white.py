from ignore_comment_line import ignore_comment_line


def ignore_white(lines):
    position = 0
    for l in lines:
        lines[position] = l.replace(" ", "").replace("\n", "")
        position += 1
    return lines
