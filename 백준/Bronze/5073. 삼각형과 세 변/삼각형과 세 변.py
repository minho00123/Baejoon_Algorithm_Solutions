while True:
  n_list = sorted(list(map(int, input().split())))
  if sum(n_list) == 0:
    break
  else:
    if n_list[2] >= n_list[1] + n_list[0]:
      print('Invalid')
    elif n_list[2] == n_list[1] and n_list[2] == n_list[0]:
      print('Equilateral')
    elif n_list[2] == n_list[1] or n_list[2] == n_list[1] or n_list[1] == n_list[0]:
      print('Isosceles')
    else:
      print('Scalene')