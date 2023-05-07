for i in range(3):
  n_list = list(map(int, input().split()))
  cnt_back = n_list.count(0)
  if cnt_back == 1:
    print('A')
  elif cnt_back == 2:
    print('B')
  elif cnt_back == 3:
    print('C')
  elif cnt_back == 4:
    print('D')
  else:
    print('E')
