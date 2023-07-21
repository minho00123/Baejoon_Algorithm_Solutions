T = int(input())
for i in range(1, T+1):
  l = list(input().split())
  if l[1] == '+':
    if int(l[0]) + int(l[2]) == int(l[4]):
      print(f'Case {i}: YES')
    else:
      print(f'Case {i}: NO')
  elif l[1] == '-':
    if int(l[0]) - int(l[2]) == int(l[4]):
      print(f'Case {i}: YES')
    else:
      print(f'Case {i}: NO')