while True:
  n = int(input())
  if n == -1:
    break
  else:
    t_bf = 0
    d = 0
    for _ in range(n):
      s, t = map(int, input().split())
      d += s * (t - t_bf)
      t_bf = t
    print(d, 'miles')