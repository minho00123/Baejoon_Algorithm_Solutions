N = int(input())
for i in range(N):
  P, C = map(float, input().split())
  O = (100 * P) / (C + 100)
  print(f'{O:0.9f}')
