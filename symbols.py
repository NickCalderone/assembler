from make_symbol_dict import make_symbol_dict
from make_dictionary import make_dictionary
from remove_symbols import remove_symbols
from replace_symbols import replace_symbols


def symbols(lines):
    dictionary = make_symbol_dict(lines)
    complete_dictionary = make_dictionary(lines, dictionary)
    del_symbols = remove_symbols(lines)
    replaced = replace_symbols(del_symbols, complete_dictionary)
    return replaced

