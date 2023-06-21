def solution(n):
    i = n // 7
    j = n % 7
    if j == 0:
        return i
    else:
        return i + 1