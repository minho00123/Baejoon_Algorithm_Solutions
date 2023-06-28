N = int(input())
total = 0
for _ in range(N):
  s, a = map(int, input().split())
  total += a % s
print(total)