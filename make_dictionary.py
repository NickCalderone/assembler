def make_dictionary(lines, dictionary):
    value = dictionary
    location = 16
    for l in lines:
        if l[0] == '@' and l[1].isalpha() is True:
            if l[1:] not in value:
                value[l[1:]] = location
                location += 1
    print("complete_dictionary/n", value)
    return value
