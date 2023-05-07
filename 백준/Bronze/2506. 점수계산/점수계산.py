N = int(input())
n_list = list(map(int, input().split()))
score = n_list[0]
is_cont = 0
for i in range(1, N):
  if n_list[i - 1] == 1 and n_list[i] == 1:
    is_cont += 1
  else:
    is_cont = 0
  score += is_cont + n_list[i]

print(score)
