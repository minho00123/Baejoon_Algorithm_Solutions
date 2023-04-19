n = int(input())
for i in range(n):
  t = list(map(int, input().split()))
  print('Denominations: ', end = '')
  for j in range(1, len(t)):
    print(t[j], end = ' ')
  flag = 0
  prev = t[1]
  for k in range(2, len(t)):
    if t[k] < 2 * prev:
      flag = 1
      break
    prev = t[k]
  print()
  if flag == 1:
    print('Bad coin denominations!')
  else:
    print('Good coin denominations!')
  print()
