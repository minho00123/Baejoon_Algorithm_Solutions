tc = int(input())
for _ in range(tc):
  n, l = input().split()
  n = int(n)
  l = ord(l)
  print(chr(l))
  for i in range(2, n+1):
    l = ((l + 1 - 65) % 26) + 65
    print(chr(l) * i)
  print()