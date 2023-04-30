N = int(input())
N_lst = list(map(int, input().split()))
box_cnt = 0
for i in range(1, N):
  if N_lst[i - 1] < N_lst[i]:
    box_cnt += 1
print(box_cnt)
