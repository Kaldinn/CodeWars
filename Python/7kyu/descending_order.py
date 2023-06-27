def descending_order(num):
    string = str(num)
    arry = [item for item in string]
    arry.sort(reverse=True)
    string = ''
    for item in arry:
       string += item
    print (int(string))
descending_order(51)