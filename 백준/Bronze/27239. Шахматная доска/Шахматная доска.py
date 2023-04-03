board = [0] * 65
num = ['1', '2', '3', '4', '5', '6', '7', '8']
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

cnt = 1
n_cnt = 0
while cnt < 65:
  a_cnt = 0
  while a_cnt < 8:
    board[cnt] = alpha[a_cnt] + num[n_cnt]
    a_cnt += 1
    cnt += 1
  n_cnt += 1

n = int(input())
print(board[n])