def solution(numLog):
    answer = ''
    l = len(numLog)
    num = numLog[0]
    for i in range(1, l):
        diff = numLog[i] - num
        if diff == 1:
            answer += 'w'
        elif diff == -1:
            answer += 's'
        elif diff == 10:
            answer += 'd'
        elif diff == -10:
            answer += 'a'
        num = numLog[i]
    return answer