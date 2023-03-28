N = int(input())
for i in range(N):
  c, r = map(int, input().split())
  for j in range(r):
    for k in range(c):
      print('X', end='')
    print()
  print()
