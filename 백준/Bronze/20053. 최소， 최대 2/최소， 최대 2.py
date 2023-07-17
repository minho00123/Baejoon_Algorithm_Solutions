T = int(input())
for _ in range(T):
  N = int(input())
  N_list = list(map(int, input().split()))
  print(min(N_list), max(N_list))