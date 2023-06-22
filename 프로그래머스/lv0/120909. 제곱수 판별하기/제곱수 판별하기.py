def solution(n):
    flag = 0
    for i in range(1, (n // 2) + 1):
        if i**2 == n:
            flag = 1
    if flag == 1:
        return 1
    else:
        return 2