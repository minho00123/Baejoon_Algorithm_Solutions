A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())
cost_X = A * P
cost_Y = 0
if P > C:
  cost_Y = B + ((P - C) * D)
else:
  cost_Y = B

print(min(cost_X, cost_Y))