N = int(input())
for _ in range(N):
  print('@'*(N*3) + ' '*N + '@'*N)
for _ in range(N*3):
  print('@'*N + ' '*N + '@' * N + ' '*N + '@'*N)
for _ in range(N):
  print('@'*N + ' '*N + '@'*(N*3))