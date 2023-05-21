num_list = sorted(list(map(int, input().split())))
sum_num = min(num_list[1] - num_list[0] , num_list[2] - num_list[1])

for i in range(3):
  temp = num_list[i]
  if temp + sum_num not in num_list:
    print(temp + sum_num)
    break