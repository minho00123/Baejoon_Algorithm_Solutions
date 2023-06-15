n = int(input())
for _ in range(n):
  d = int(input())
  cnt = 0
  for i in range(1, d+1):
    if d % i == 0:
      cnt += 1
  print(d, cnt)