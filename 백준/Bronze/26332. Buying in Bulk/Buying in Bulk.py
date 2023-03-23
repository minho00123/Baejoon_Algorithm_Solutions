n = int(input())
for i in range(n):
  c, p = map(int, input().split())
  total_cost = c * p
  print(c, p)
  if c == 1:
    print(total_cost)
  else:
    print(total_cost - ((c - 1) * 2))
