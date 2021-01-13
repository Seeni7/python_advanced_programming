from random import shuffle as l_shuffle

str_value = 'Kevin Bacon'
def reverse(str_vaue):
    return str_value[::-1]

def str_shuffle(str_vlaue):
    str_list = list(str_value)
    l_shuffle(str_list)
    return "".join(str_list)