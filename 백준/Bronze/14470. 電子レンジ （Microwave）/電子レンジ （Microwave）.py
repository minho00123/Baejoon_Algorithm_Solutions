A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
warm_time = 0
if A < 0:
  A *= -1
  warm_time = D + (A * C) + (B * E)
  print(warm_time)
else:
  warm_time = (B - A) * E
  print(warm_time)
