str = input()
cnt_lst = [0] * 26

for i in range(len(str)):
  index_c = ord(str[i]) - 97
  cnt_lst[index_c] += 1

cnt_even = 0
cnt_odd = 0
for i in range(len(cnt_lst)):
  if cnt_lst[i] == 0:
    continue
  elif cnt_lst[i] % 2 == 0:
    cnt_even += 1
  elif cnt_lst[i] % 2 == 1:
    cnt_odd += 1

if cnt_even > 0 and cnt_odd == 0:
  print(0)
elif cnt_even == 0 and cnt_odd > 0:
  print(1)
else:
  print(2)
