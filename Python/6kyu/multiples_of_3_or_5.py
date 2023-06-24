def solution(number):
    my_list = [item for item in range(1, number) if item % 3 == 0 or item % 5 == 0]
    return sum(my_list)





  