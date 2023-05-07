N = int(input())
award = [0] * N
for i in range(N):
  n1, n2, n3 = map(int, input().split())
  if n1 == n2 and n1 == n3:
    award[i] = 10000 + (n1 * 1000)
  elif n1 == n2 or n1 == n3:
    award[i] = 1000 + (n1 * 100)
  elif n2 == n3:
    award[i] = 1000 + (n2 * 100)
  else:
    award[i] = max(n1, n2, n3) * 100

print(max(award))
