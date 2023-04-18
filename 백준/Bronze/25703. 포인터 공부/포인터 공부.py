N = int(input())
star = '*'
print('int a;')
if N == 1:
  print('int *ptr = &a;')
elif N == 2:
  print('int *ptr = &a;')
  print('int **ptr2 = &ptr;')
else:
  print('int *ptr = &a;')
  print('int **ptr2 = &ptr;')
  for i in range(2, N):
    print(f'int {star * (i + 1)}ptr{i + 1} = &ptr{i};')