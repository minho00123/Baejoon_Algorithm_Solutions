from sys import stdin

for i in range(3):
  N = int(stdin.readline())
  s = 0
  for i in range(N):
    s += int(stdin.readline())

  if s == 0:
    print('0')
  elif s > 0:
    print('+')
  else:
    print('-')
