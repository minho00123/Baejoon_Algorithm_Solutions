i = 1
while True:
  n = int(input())
  n4 = 0
  if n == 0:
    break
  else:
    if n % 2 == 0:
      n4 = n // 2
      print(f'{i}. even {n4}')
    else:
      n4 = (n-1) // 2
      print(f'{i}. odd {n4}')
  i += 1