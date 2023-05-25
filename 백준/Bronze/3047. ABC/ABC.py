num_list = sorted(list(map(int, input().split())))
str = input()

for i in range(3):
  if str[i] == 'A':
    print(num_list[0], end=' ')
  elif str[i] == 'B':
    print(num_list[1], end=' ')
  else:
    print(num_list[2], end=' ')