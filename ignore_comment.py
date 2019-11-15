def ignore_comment(key):
    value = list(filter(lambda x: x[0] != "/" and x[1] != "/", key))
    return value
