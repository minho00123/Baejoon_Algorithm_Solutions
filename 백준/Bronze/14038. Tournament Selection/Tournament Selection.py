win_cnt = 0
for i in range(6):
  s = input()
  if s == 'W':
    win_cnt += 1

if win_cnt >= 5:
  print(1)
elif win_cnt >= 3:
  print(2)
elif win_cnt >= 1:
  print(3)
else:
  print(-1)
