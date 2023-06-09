t = int(input())
for _ in range(t):
  n_list = list(map(int, input().split()))
  odd_s = 0
  even_s = 0
  for i in range(1, len(n_list)):
    if n_list[i] % 2 == 1:
      odd_s += n_list[i]
    else:
      even_s += n_list[i]

  if odd_s > even_s:
    print('ODD')
  elif odd_s < even_s:
    print('EVEN')
  else:
    print('TIE')