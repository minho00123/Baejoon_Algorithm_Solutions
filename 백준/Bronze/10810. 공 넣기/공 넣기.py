N, M = map(int, input().split())
N_list = [0] * (N + 1)
for _ in range(M):
  i, j, k = map(int, input().split())
  for l in range(i, j+1):
    N_list[l] = k

for i in range(1, len(N_list)):
  print(N_list[i], end=' ')