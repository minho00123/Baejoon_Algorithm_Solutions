def solution(n):
    n = str(n)
    answer = 0
    for i in range(len(n)):
        print(n[i])
        answer += int(n[i])
    return answer