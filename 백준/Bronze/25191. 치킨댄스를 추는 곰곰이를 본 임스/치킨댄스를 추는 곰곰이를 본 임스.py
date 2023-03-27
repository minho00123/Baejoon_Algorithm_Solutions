N = int(input())
A, B = map(int, input().split())
max_num = (A // 2) + B
if N <= max_num:
  print(N)
else:
  print(max_num)
