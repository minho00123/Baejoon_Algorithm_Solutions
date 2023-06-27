N = int(input())
for _ in range(N):
  r, e, c = map(int, input().split())
  ad = e - c
  if r > ad:
    print('do not advertise')
  elif r < ad:
    print('advertise')
  else:
    print('does not matter')