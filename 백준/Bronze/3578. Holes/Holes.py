h = int(input())
if h == 0:
  print(1)
elif h == 1:
  print(0)
elif h % 2 == 1:
  eight = h // 2 * '8'
  print(f'4{eight}')
else:
  eight = h // 2 * '8'
  print(eight)