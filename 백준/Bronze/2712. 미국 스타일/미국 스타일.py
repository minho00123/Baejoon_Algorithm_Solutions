N = int(input())
for i in range(N):
  n, u = input().split()
  n = float(n)
  if u == 'kg':
    n = n * 2.2046
    print(f'{n:0.4f} lb')
  elif u == 'lb':
    n = n * 0.4536
    print(f'{n:0.4f} kg')
  elif u == 'l':
    n = n * 0.2642
    print(f'{n:0.4f} g')
  elif u == 'g':
    n = n * 3.7854
    print(f'{n:0.4f} l')
