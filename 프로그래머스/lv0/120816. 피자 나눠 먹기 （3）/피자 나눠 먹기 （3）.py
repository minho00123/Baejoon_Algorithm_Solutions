def solution(slice, n):
    i = n // slice
    j = n % slice
    if j == 0:
        return i
    else:
        return i + 1