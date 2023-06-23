def solution(my_string, s, e):
    answer = ''
    l = len(my_string)
    for i in range(s):
        answer += my_string[i]
    for i in range(e, s-1, -1):
        answer += my_string[i]
    for i in range(e+1, l):
        answer += my_string[i]
    return answer