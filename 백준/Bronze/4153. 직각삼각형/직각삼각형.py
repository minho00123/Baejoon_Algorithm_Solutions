while True:
  n_list = list(map(int, input().split()))
  n_list.sort()
  if sum(n_list) == 0:
    break
  else:
    if n_list[0]**2 + n_list[1]**2 == n_list[2]**2:
      print('right')
    else:
      print('wrong')