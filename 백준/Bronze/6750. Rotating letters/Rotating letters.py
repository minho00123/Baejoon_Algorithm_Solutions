check_l = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
s = input()
flag = 0
for i in range(len(s)):
  for j in range(7):
    if s[i] == check_l[j]:
      flag += 1

if flag == len(s):
  print('YES')
else:
  print('NO')