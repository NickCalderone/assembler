def ignore_after_comment(lines):
    value = []
    for l in lines:
        value.append(l.split('//')[0])
    return value
