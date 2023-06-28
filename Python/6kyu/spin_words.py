def spin_words(sentence):
    splited = sentence.split(" ")
    word = ""
    for item in splited:
        if len(item) < 5:
            word += item
            word += " "
        elif len(item) >=5:
            new_item = item[::-1]
            word += new_item
            word += " "
    final = word[:-1]
    return final


