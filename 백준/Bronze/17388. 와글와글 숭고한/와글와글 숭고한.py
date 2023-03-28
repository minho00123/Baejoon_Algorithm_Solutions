univ_lst = list(map(int, input().split()))
s = 0
for i in range(3):
  s += univ_lst[i]
if s >= 100:
  print('OK')
else:
  min_i = -1
  for i in range(3):
    if min(univ_lst) == univ_lst[i]:
      min_i = i
  if min_i == 0:
    print('Soongsil')
  elif min_i == 1:
    print('Korea')
  else:
    print('Hanyang')