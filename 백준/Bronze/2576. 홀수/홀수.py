odd_num = []
for i in range(7):
  n = int(input())
  if n % 2 == 1:
    odd_num.append(n)

if len(odd_num) == 0:
  print(-1)
else:
  print(sum(odd_num))
  print(min(odd_num))
