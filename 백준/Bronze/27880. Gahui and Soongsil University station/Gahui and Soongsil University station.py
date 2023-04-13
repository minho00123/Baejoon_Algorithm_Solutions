total = 0
for i in range(4):
  w, n = input().split()
  if w == "Es":
    total += int(n) * 21
  elif w == "Stair":
    total += int(n) * 17
print(total)
