tc = int(input())
for _ in range(tc):
  n = int(input())
  ans = []
  for i in range(n):
    for j in range(n):
      if i + j == n and i < j:
        ans.append(f'{i} {j}')
  ans_s = ', '.join(ans)
  print(f'Pairs for {n}: {ans_s}')