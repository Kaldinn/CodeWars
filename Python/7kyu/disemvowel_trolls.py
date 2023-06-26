def disemvowel(string_):
    vowels = ["a", "e","i","o","u"]
    arry = []
    str = ''
    for letter in string_:
        arry.append(letter)
        if letter.lower() in vowels:
            arry.remove(letter)
    for items in arry:
        str += items
    return(str)
    

disemvowel("This website is for losers LOL!")