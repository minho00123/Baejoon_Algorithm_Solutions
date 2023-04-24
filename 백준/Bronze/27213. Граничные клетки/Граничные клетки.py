m = int(input())
n = int(input())
ans = ((m*2) + (n*2)) - 4
if m == 1 or n == 1:
  ans = (m+n) - 1
print(ans)