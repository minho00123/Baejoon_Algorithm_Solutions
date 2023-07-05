K = int(input())
N = int(input())
T_list = []
Z_list = []
for _ in range(N):
  T, Z = input().split()
  T_list.append(int(T))
  Z_list.append(Z)
  
total_t = 0
for i in range(len(T_list)):
  total_t += T_list[i]
  if total_t >= 210:
    break
  else:
    if Z_list[i] == 'T':
      K = (K % 8) + 1
print(K)