def isogram_check(word):
    list = []
    for letter in word:
        letters = letter.lower()
        if letters in list:
            return False
        else:
            list.append(letters)
    return True
 



def is_isogram(string):
    return len(string) == len(set(string.lower()))




