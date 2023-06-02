T = int(input())
for _ in range(T):
  n = int(input())
  b_n = bin(n)
  l = len(b_n)
  j = 0
  for i in range(l - 1, 1, -1):
    if b_n[i] == '1':
      print(j, end=' ')
    j += 1
  print()