def open_file(filename):
    """open and parse file, return as list of lines"""
    line_list = []
    with open(filename, 'r') as list_file:
        for line in list_file:
            line_list.append(line)
        return line_list


def readcurrency(filename):
    """take list of lines, process further, add to dictionaries within a list"""
    input_list = open_file("currency.txt")
    currency_dict = []
    for item in input_list:
        temp = item.split()
        currency_dict.append({"symbol":temp[0], "rate":temp[1]})
    return currency_dict
    

print(readcurrency("currency.txt"))