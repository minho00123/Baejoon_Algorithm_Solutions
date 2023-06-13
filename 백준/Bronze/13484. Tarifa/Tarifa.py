X = int(input())
N = int(input())
ans = X * (N + 1)
for _ in range(N):
  P = int(input())
  ans -= P
print(ans)