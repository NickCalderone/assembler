def remove_symbols(lines):
    no_symbols = []
    for l in lines:
        if l[0] != '(':
            no_symbols.append(l)
    print('del_symbols', no_symbols)
    return no_symbols
