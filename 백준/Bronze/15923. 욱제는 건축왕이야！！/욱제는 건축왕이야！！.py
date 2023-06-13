N = int(input())
x = []
y = []
for _ in range(N):
  n1, n2 = map(int, input().split())
  x.append(n1)
  y.append(n2)
real_x = max(x) - min(x)
real_y = max(y) - min(y)
print(2 * real_x + 2 * real_y)