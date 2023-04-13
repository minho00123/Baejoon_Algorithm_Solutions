import math

K = int(input())
for i in range(1, K + 1):
  n, s, d = map(int, input().split())
  total_pay = 0
  for k in range(n):
    dist, v = map(int, input().split())
    if math.ceil(dist / s) <= d:
      total_pay += v
  print(f'Data Set {i}:')
  print(total_pay)
  print()
