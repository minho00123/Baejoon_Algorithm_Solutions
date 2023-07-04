T = int(input())
for _ in range(T):
  n_list = list(map(int, input().split()))
  tmp_list = []
  for i in range(4):
    tmp_list.append(n_list[i] + n_list[i + 4])
  if tmp_list[0] < 1:
    tmp_list[0] = 1
  if tmp_list[1] < 1:
    tmp_list[1] = 1
  if tmp_list[2] < 0:
    tmp_list[2] = 0
  ans = tmp_list[0] + 5*tmp_list[1] + 2*tmp_list[2] + 2*tmp_list[3]
  print(ans)