while True:
  l, w, a = map(int, input().split())
  if l == 0 and w == 0 and a == 0:
    break
  else:
    if l == 0:
      l = a // w
      print(l, w, a)
    elif w == 0:
      w = a // l
      print(l, w, a)
    else:
      a = l * w
      print(l, w, a)