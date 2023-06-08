while True:
  str = input()
  if str == '***':
    break
  else:
    for i in range(len(str)-1, -1, -1):
      print(str[i], end='')
  print()