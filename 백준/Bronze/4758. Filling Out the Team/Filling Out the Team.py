while True:
  speed, weight, strength = map(float, input().split())
  if speed == 0 and weight == 0 and strength == 0:
    break
  else:
    cnt = 0
    if speed <= 4.5 and weight >= 150 and strength >= 200:
      print('Wide Receiver', end=' ')
      cnt += 1
    if speed <= 6 and weight >= 300 and strength >= 500:
      print('Lineman', end=' ')
      cnt += 1
    if speed <= 5 and weight >= 200 and strength >= 300:
      print('Quarterback', end=' ')
      cnt += 1
    if cnt == 0:
      print('No positions', end=' ')
  print()