T = int(input())
for i in range(T):
  n = list(map(int, input().split()))
  even_num = []
  for i in range(7):
    if n[i] % 2 == 0:
      even_num.append(n[i])
  print(sum(even_num), min(even_num))