import math

N, W, H = map(int, input().split())
D = math.sqrt(W**2 + H**2)
for _ in range(N):
  n = int(input())
  if n <= W or n <= H or n <= D:
    print('YES')
  else:
    print('NO')