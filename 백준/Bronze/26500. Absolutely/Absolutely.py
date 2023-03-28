n = int(input())
for i in range(n):
  n1, n2 = map(float, input().split())
  dist = abs(n2 - n1)
  print(f'{dist:.1f}')
