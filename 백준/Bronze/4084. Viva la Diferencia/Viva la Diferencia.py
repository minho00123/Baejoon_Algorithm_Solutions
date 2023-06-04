while True:
  n_list = list(map(int, input().split()))
  if sum(n_list) == 0:
    break
  cnt = 0
  while True:
    if n_list[0] == n_list[1] and n_list[1] == n_list[2] and n_list[2] == n_list[3]:
      print(cnt)
      break
    else:
      tmp = n_list[0]
      n_list[0] = abs(n_list[0] - n_list[1])
      n_list[1] = abs(n_list[1] - n_list[2])
      n_list[2] = abs(n_list[2] - n_list[3])
      n_list[3] = abs(n_list[3] - tmp)
      cnt += 1