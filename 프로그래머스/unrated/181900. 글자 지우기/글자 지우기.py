def solution(my_string, indices):
    str_list = list(my_string)
    for i in range(len(indices)):
        str_list[indices[i]] = ''
    answer = ''.join(str_list)
    return answer