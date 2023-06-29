V = int(input())
v = input()
A_cnt = 0
B_cnt = 0
for i in range(V):
  if v[i] == 'A':
    A_cnt += 1
  elif v[i] == 'B':
    B_cnt += 1

if A_cnt > B_cnt:
  print('A')
elif A_cnt < B_cnt:
  print('B')
else:
  print('Tie')