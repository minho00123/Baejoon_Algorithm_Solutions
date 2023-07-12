N = int(input())
for _ in range(N):
  n = input()
  m = len(n) // 2
  if n[m] == n[m - 1]:
    print('Do-it')
  else:
    print('Do-it-Not')