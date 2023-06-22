def solution(n):
    comp_num = []
    for i in range(4, 101):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt >= 3:
            comp_num.append(i)
    answer = 0
    for i in range(len(comp_num)):
        if comp_num[i] <= n:
            answer += 1
        else:
            break
    return answer