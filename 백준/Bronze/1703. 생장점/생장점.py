while True:
  a_lst = list(map(int, input().split()))
  if a_lst[0] == 0:
    break;
  leaves = 1
  for i in range(1, len(a_lst), 2):
    leaves = leaves * a_lst[i] - a_lst[i+1]
  print(leaves)
