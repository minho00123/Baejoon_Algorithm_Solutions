n = int(input())
if n == 1010:
  print(20)
elif n < 100:
  print((n // 10) + (n % 10))
elif n > 100 and n < 110:
  print(10 + (n % 10))
else:
  print(10 + (n // 100))
