s = input()
for i in range(4):
  if s[i] == 'E':
    print('I', end='')
  elif s[i] == 'I':
    print('E', end='')
  elif s[i] == 'S':
    print('N', end='')
  elif s[i] == 'N':
    print('S', end='')
  elif s[i] == 'T':
    print('F', end='')
  elif s[i] == 'F':
    print('T', end='')
  elif s[i] == 'J':
    print('P', end='')
  elif s[i] == 'P':
    print('J', end='')