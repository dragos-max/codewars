# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

def filter_list(l):
    l2 = []
    for item in l:
        if isinstance(item, int):
            l2.append(item)     
    return l2
