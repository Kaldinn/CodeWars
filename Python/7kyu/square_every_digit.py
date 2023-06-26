def square_digits(num):
    string = str(num)
    string.join(',')
    arry = []
    int_arry = []
    new_arry = []
    for item in string:
        arry.append(item)
        int_item = int(item)
        int_item *= int_item
        int_arry.append(int_item)
    
    for item in int_arry:
        x = ''.join(str(item))
        new_arry.append(x)

    z = ''.join(new_arry)
    y = int(z)
    print(type(y))


square_digits(9119)
