def solution(my_string):
    answer = list(my_string)
    l = len(answer)
    for i in range(l):
        for j in range(i+1, l):
            if answer[i] == answer[j]:
                answer[j] = ''
    answer = ''.join(answer)
    return answer