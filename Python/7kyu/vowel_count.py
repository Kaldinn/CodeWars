# def get_count(sentence):
#     vowels = ["a", "e","i","o","u"]
#     sum = 0
#     for letter in sentence:
#         if letter in vowels:
#             sum += 1
#     print(sum)

# get_count("aei23dsu")

def get_count(sentence):
    sum = 0
    answer = [sum for letter in sentence if letter in ["a", "e","i","o","u"]]
    print (len(answer))

get_count("aeio")