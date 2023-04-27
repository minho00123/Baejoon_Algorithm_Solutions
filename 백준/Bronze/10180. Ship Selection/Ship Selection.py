T = int(input())
for i in range(T):
  N, D = map(int, input().split())
  ans = 0
  for j in range(N):
    vi, fi, ci = map(int, input().split())
    if vi * fi / ci >= D:
      ans += 1
  print(ans)
