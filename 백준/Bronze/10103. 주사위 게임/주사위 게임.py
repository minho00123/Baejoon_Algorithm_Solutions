n = int(input())
chang_score = 100
sang_score = 100

for _ in range(n):
  c, s = map(int, input().split())
  if c > s:
    sang_score -= c
  elif c < s:
    chang_score -= s

print(chang_score)
print(sang_score)