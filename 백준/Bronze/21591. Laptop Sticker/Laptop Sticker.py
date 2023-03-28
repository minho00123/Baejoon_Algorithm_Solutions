wc, hc, ws, hs = map(int, input().split())
w_diff = wc - ws
h_diff = hc - hs
if w_diff <= 1 or h_diff <= 1:
  print(0)
else:
  print(1)
