a, b = map(int, input().split())
min_num = min(a, b)
if (a % 2 == 1) and (b % 2 == 1):
  print(min_num)
else:
  print(0)