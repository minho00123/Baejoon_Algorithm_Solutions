N, W, H, L = map(int, input().split())
maximum_num = (W // L) * (H // L)
if maximum_num <= N:
  print(maximum_num)
else:
  print(N)
