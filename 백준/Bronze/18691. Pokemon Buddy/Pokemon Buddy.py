for _ in range(int(input())):
  G, C, E = map(int, input().split())
  km = 0
  if G == 1:
    km += E - C
  elif G == 2:
    km += (E - C) * 3
  else:
    km += (E - C) * 5
  
  if km <= 0:
    print(0)
  else:
    print(km)
