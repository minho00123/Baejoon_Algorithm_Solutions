N = int(input())
if N == 1:
  print('*')
else:
  j = 2
  print(' ' * (N - 1) + '*')
  for i in range(N-3, -1, -1):
    print(' ' * (i + 1) + '*' + ' ' * (N - i - 2) + ' ' * (j - 2) + '*' * (N - i - j))
    j += 1
  print('*' * (N + j - 1))