a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())
if T - 30 < 0:
  print(a, end=' ')
else:
  print((T - 30) * x * 21 + a, end=' ')
if T - 45 < 0:
  print(b)
else:
  print((T - 45) * y * 21 + b)
