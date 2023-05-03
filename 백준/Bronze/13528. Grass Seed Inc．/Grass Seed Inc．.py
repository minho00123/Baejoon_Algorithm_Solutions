C = float(input())
L = int(input())
total = 0
for i in range(L):
  w, l = map(float, input().split())
  total += w * l
C = total * C
print(f'{C:0.7f}')
