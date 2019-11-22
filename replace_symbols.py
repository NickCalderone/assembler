def replace_symbols(lines, dictionary):
    replaced = []
    for l in lines:
        if l[0] == '@':
            if l[1:] in dictionary:
                replaced.append('@' + str(dictionary[l[1:]]))
            else:
                replaced.append(l)
        else:
            replaced.append(l)
    return replaced
