A = int(input())
B = int(input())
ans = (A+B) % 12
if ans == 0:
  print(12)
else:
  print(ans)