def solution(a, b):
    a, b = str(a), str(b)
    n1 = int(a + b)
    n2 = int(b + a)
    return max(n1, n2)