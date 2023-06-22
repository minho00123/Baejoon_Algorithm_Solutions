def solution(a, d, included):
    n = len(included)
    num = [a]
    for i in range(n-1):
        a += d
        num.append(a)
    answer = 0
    for i in range(n):
        if included[i]:
            answer += num[i]
    return answer