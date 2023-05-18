x, y = map(int, input().split())
min = x / y
n = int(input())
for i in range(n):
  X, Y = map(int, input().split())
  if X / Y < min:
    min = X / Y
print(f'{min * 1000:0.2f}')
