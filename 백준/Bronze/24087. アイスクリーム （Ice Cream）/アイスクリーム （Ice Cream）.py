import math

S = int(input())
A = int(input())
B = int(input())
price = 250
if S - A <= 0:
  print(price)
else:
  price += math.ceil((S - A) / B) * 100
  print(price)
