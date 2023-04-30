n = int(input())
n_lst = list(map(int, input().split()))
total_cnt = n
total_sum = 0
for i in range(n):
  if n_lst[i] == -1:
    total_cnt -= 1
  else:
    total_sum += n_lst[i]

print(total_sum / total_cnt)
