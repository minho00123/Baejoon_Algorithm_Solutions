PI = 3.1415927
i = 1
while True:
  d, r, t = map(float, input().split())
  if r == 0:
    break
  distance = d / (12 * 5280) * PI * r
  mph = distance / t * 3600
  print(f'Trip #{i}: {distance:0.2f} {mph:0.2f}')
  i += 1
