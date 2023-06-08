temp_list = []
while True:
  n = float(input())
  if n == 999:
    break
  else:
    temp_list.append(n)

for i in range(1, len(temp_list)):
  print(f'{temp_list[i] - temp_list[i - 1]:0.2f}')