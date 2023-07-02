N = int(input())
if N == 1 or N == 2:
  print(1)
else:
  i = 2
  while 2**i <= N:
    if 2**i >= N:
      break
    else:
      i += 1
  if 2**i == N:
    print(1)
  else:
    print(0)