t = int(input())
for _ in range(t):
  n = int(input())
  p1_win_cnt = 0
  p2_win_cnt = 0
  for _ in range(n):
    p1, p2 = input().split()
    if p1 == 'R' and p2 == 'S':
      p1_win_cnt += 1
    elif p1 == 'S' and p2 == 'P':
      p1_win_cnt += 1
    elif p1 == 'P' and p2 == 'R':
      p1_win_cnt += 1
    elif p1 == 'S' and p2 == 'R':
      p2_win_cnt += 1
    elif p1 == 'P' and p2 == 'S':
      p2_win_cnt += 1
    elif p1 == 'R' and p2 == 'P':
      p2_win_cnt += 1
  
  if p1_win_cnt > p2_win_cnt:
    print('Player 1')
  elif p1_win_cnt < p2_win_cnt:
    print('Player 2')
  else:
    print('TIE')
