n = int(input())
for i in range(n):
  players_n = list(map(int, input().split()))
  flag = 0
  for j in range(len(players_n)):
    print(players_n[j], end=' ')
    if players_n[j] == 18:
      flag += 18
    elif players_n[j] == 17:
      flag += 17
  print()
  if flag == 18:
    print('mack')
  elif flag == 17:
    print('zack')
  elif flag == 35:
    print('both')
  elif flag == 0:
    print('none')
  print()
