N = int(input())
t = 0
for i in range(1, N+1):
  for j in range(i+1):
    t += i + j
print(t)