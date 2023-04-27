total_costs = 0
for _ in range(int(input())):
  H, B, K = map(int, input().split())
  if B > H:
    total_costs += (B - H) * K
print(total_costs)
