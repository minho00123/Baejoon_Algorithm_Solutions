P = int(input())
for i in range(P):
  K, N = map(int, input().split())
  total_candles = N
  for j in range(1, N + 1):
    total_candles += j
  print(K, total_candles)
