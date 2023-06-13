N = int(input())
k = int(input())
s = N
for _ in range(k):
  s += N * 10
  N = N * 10
print(s)