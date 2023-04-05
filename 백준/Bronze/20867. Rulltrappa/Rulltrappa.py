M, S, G = map(float, input().split())
A, B = map(float, input().split())
L, R = map(float, input().split())

left = 0
right = 0

if M % G != 0:
  left = (M/G + 1) + (L/A)
else:
  left = (M/G) + (L/A)

if M % S != 0:
  right = (M/S + 1) + (R/B)
else:
  right = (M/S) + (R/B)

if left > right:
  print('latmask')
else:
  print('friskus')
