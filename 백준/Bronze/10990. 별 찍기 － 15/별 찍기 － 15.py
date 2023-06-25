N = int(input())
j = 1
print(' ' * (N - 1) + '*')
for i in range(N-2, -1, -1):
  print(' ' * i + '*' + ' ' * (N - i - 1) + ' ' * (N - i - 2) + '*' * (N - i - j))
  j += 1