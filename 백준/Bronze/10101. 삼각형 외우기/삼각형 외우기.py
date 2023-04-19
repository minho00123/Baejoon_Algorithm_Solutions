a1 = int(input())
a2 = int(input())
a3 = int(input())
s = a1 + a2 + a3
if a1 == 60 and a2 == 60 and a3 == 60:
  print('Equilateral')
elif s == 180:
  if ((a1 == a2) or (a1 == a3) or (a2 == a3)):
    print('Isosceles')
  else:
    print('Scalene')
else:
  print('Error')
