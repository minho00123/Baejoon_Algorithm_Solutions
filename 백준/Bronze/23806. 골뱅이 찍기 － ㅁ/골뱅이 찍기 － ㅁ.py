N = int(input())
for _ in range(N):
  print('@' * (N * 5))
for _ in range(N*3):
  print('@' * N + ' ' * (N * 3) + '@' * N)
for _ in range(N):
  print('@' * (N * 5))