n = int(input())
for i in range(n):
  stats = list(map(int, input().split()))
  is_over_ten = 0
  for i in range(3):
    print(stats[i], end=' ')
    if stats[i] >= 10:
      is_over_ten += 1
  print()
  if is_over_ten == 0:
    print('zilch')
  elif is_over_ten == 1:
    print('double')
  elif is_over_ten == 2:
    print('double-double')
  else:
    print('triple-double')
  print()
 