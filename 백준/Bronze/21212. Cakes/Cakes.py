N = int(input())
tmp = []
for _ in range(N):
  n1, n2 = map(int, input().split())
  tmp.append(n2 // n1)
print(min(tmp))