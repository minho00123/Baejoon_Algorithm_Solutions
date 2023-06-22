def solution(my_string, m, c):
    str_list = []
    for i in range(0, len(my_string), m):
        str_list.append(my_string[i:i+m])
    answer = ''
    for i in range(len(str_list)):
        answer += str_list[i][c-1]
    return answer
    