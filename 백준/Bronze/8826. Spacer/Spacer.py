Z = int(input())
for _ in range(Z):
  n = int(input())
  i = input()
  cnt_N = 0
  cnt_S = 0
  cnt_W = 0
  cnt_E = 0
  for j in range(len(i)):
    if i[j] == 'N':
      cnt_N += 1
    elif i[j] == 'S':
      cnt_S += 1
    elif i[j] == 'W':
      cnt_W += 1
    else:
      cnt_E += 1
  print(abs(cnt_N - cnt_S) + abs(cnt_W - cnt_E))