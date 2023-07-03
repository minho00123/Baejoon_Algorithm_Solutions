n = int(input())
for i in range(1, n+1):
  n_list = sorted(list(map(int, input().split())))
  if n_list[0]**2 + n_list[1]**2 == n_list[2]**2:
    print(f'Scenario #{i}:')
    print('yes\n')
  else:
    print(f'Scenario #{i}:')
    print('no\n')