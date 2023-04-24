import math

A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())
slice = P1 / A1
whole = P2 / (R1**2*math.pi)
if slice < whole:
  print('Slice of pizza')
else:
  print('Whole pizza')
