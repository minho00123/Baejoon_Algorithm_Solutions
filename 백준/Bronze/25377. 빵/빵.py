N = int(input())
ans = 1001
for i in range(N):
  A, B = map(int, input().split())
  if A <= B:
    if B < ans:
      ans = B

if ans == 1001:
  print(-1)
else:
  print(ans)
