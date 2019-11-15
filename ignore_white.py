from ignore_comment import ignore_comment


def ignore_white(lines):
    position = 0
    for l in lines:
        lines[position] = l.replace(" ", "").replace("\n", "")
        position += 1
    return lines
