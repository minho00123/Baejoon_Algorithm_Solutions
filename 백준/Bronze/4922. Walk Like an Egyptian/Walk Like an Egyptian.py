while True:
  N = int(input())
  if N == 0:
    break
  else:
    ans = N**2 - (N - 1)
    print(f'{N} => {ans}')