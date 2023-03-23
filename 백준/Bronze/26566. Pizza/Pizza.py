import math

n = int(input())
for i in range(n):
  A1, P1 = map(int, input().split())
  R1, P2 = map(int, input().split())
  slice_pizza_amount = A1 / P1
  whole_pizza_amount = (pow(R1, 2) * math.pi) / P2
  if slice_pizza_amount > whole_pizza_amount:
    print('Slice of pizza')
  else:
    print('Whole pizza')
