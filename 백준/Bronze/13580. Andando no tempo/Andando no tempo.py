num_lst = list(map(int, input().split()))
flag = 0
if num_lst[0] - num_lst[1] == 0:
  flag = 1
elif num_lst[0] - num_lst[2] == 0:
  flag = 1
elif num_lst[1] - num_lst[2] == 0:
  flag = 1
elif (num_lst[0] - (num_lst[1] + num_lst[2])) == 0:
  flag = 1
elif (num_lst[1] - (num_lst[0] + num_lst[2])) == 0:
  flag = 1
elif (num_lst[2] - (num_lst[0] + num_lst[1])) == 0:
  flag = 1
  
if flag:
  print('S')
else:
  print('N')
