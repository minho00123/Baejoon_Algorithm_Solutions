def solution(a, b):
    n1 = 2 * a * b
    a, b = str(a), str(b)
    n2 = int(a+b)
    return max(n1, n2)