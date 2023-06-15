N = int(input())
for _ in range(N):
  a1, a2, a3 = map(int, input().split())
  if a1 + a2 + a3 == 180:
    print(a1, a2, a3, 'Seems OK')
  else:
    print(a1, a2, a3, 'Check')