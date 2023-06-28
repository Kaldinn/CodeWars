def accum(s):
    arry = [item.upper() + item.lower() * index for index, item in enumerate(s)]
    return '-'.join(arry)
