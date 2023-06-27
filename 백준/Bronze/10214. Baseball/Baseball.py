T = int(input())
for _ in range(T):
  Y_win = 0
  K_win = 0
  for i in range(9):
    Y, K = map(int, input().split())
    Y_win += Y
    K_win += K
  
  if Y_win > K_win:
    print('Yonsei')
  elif Y_win < K_win:
    print('Korea')
  else:
    print('Draw')