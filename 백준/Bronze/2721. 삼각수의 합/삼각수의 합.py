N = int(input())
for i in range(N):
  n = int(input())
  W = 0
  T = 1
  for j in range(1, n+1):
    T += j + 1
    W += j * T
  print(W)
