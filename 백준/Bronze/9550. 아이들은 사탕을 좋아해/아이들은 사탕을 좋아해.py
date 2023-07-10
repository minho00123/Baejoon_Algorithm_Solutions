T = int(input())
for _ in range(T):
  N, K = map(int, input().split())
  n = list(map(int, input().split()))
  ans = 0
  for i in range(N):
    if n[i] >= K:
      ans += n[i] // K
  print(ans)