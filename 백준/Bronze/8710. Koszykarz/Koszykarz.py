k, w, m = map(int, input().split())
quo = (w - k) // m
rem = (w - k) % m
if rem != 0:
  print(quo + 1)
else:
  print(quo)