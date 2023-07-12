N = int(input())
l = []
for _ in range(N):
  l.append(input())
K = int(input())
if K == 1:
  for i in range(N):
    print(l[i])
elif K == 2:
  for i in range(N):
    print(l[i][::-1])
elif K == 3:
  for i in range(N-1, -1, -1):
    print(l[i])