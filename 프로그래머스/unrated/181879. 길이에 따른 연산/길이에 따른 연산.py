def solution(num_list):
    l = len(num_list)
    if l >= 11:
        return sum(num_list)
    else:
        answer = 1
        for i in range(l):
            answer *= num_list[i]
        return answer