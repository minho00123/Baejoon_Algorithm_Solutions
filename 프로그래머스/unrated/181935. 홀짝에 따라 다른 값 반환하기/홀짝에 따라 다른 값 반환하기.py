def solution(n):
    if n % 2 == 1:
        ans = 0
        for i in range(n+1):
            if i % 2 == 1:
                ans += i
        return ans
    else:
        ans = 0
        for i in range(n+1):
            if i % 2 == 0:
                ans += i**2
        return ans