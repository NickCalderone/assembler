def bin_destination(destination):
    switcher = {
        'null': '000',
        'M': '001',
        'D': '010',
        'MD': '011',
        'A': '100',
        'AM': '101',
        'AD': '110',
        'AMD': '111'
    }
    return switcher.get(destination, "bin_destination error")
