# def digital_root(n):
#     arry = []
#     arry.append(n)
#     split_list = list(map(int, str(arry[0])))
#     result = sum(split_list)

#     if result < 10:
#         return result

#     elif sum(split_list) >= 10:
#         new_arry = []
#         new_arry.append(sum(split_list))
#         new_split_list = list(map(int,str(new_arry[0])))
#         new_result = sum(new_split_list)
        
#         if new_result >= 10:
#             new_new_arry = []
#             new_new_arry.append(sum(new_split_list))
#             new_new_split_list = list(map(int,str(new_new_arry[0])))
#             new_new_result = sum(new_new_split_list)
#             return (new_new_result)
#         else:
#             return new_result

    

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

digital_root(493193)