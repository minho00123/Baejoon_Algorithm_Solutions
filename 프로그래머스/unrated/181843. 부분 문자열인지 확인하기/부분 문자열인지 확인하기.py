def solution(my_string, target):
    if my_string.find(target) != -1:
        return 1
    elif my_string:
        return 0