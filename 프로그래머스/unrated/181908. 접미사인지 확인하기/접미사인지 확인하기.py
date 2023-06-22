def solution(my_string, is_suffix):
    l_str = len(my_string)
    l_suffix = len(is_suffix)
    if my_string[l_str-l_suffix:] == is_suffix:
        return 1
    else:
        return 0