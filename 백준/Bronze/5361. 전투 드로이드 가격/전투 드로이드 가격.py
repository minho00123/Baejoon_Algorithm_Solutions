costs = [350.34, 230.90, 190.55, 125.30, 180.90]

tc = int(input())
for _ in range(tc):
  total_cost = 0
  n_list = list(map(int, input().split()))
  for i in range(5):
    total_cost += costs[i] * n_list[i]
  print(f'${total_cost:0.2f}')