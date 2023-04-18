num = input()
zero_cnt = 0
last_zero_cnt = 0
for i in range(len(num) - 1, -1, -1):
  if num[i] == "0":
    last_zero_cnt += 1
  else:
    break

for i in range(len(num)):
  if num[i] == "0":
    zero_cnt += 1

print(zero_cnt - last_zero_cnt)