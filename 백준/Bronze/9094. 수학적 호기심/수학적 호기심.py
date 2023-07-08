import sys
input = sys.stdin.readline

for _ in range(int(input())):
  n, m = map(int, input().split())
  cnt = 0
  for i in range(1, n-1):
    for j in range(i+1, n):
      if (i**2 + j**2 + m) % (i * j) == 0:
        cnt += 1
  print(cnt)