n1, n2 = map(int, input().split())
per_dist = abs((((n2 - 1) // 4 + 1) - ((n1 - 1) // 4 + 1))) + abs(((n2 - 1) % 4 - (n1 - 1) % 4))
print(per_dist)
