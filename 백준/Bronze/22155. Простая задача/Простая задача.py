n = int(input())
for j in range(n):
  i, f = map(int, input().split())
  if (i <= 1) and (f <= 2):
    print('Yes')
  elif (i <= 2) and (f <= 1):
    print('Yes')
  else:
    print('No')
