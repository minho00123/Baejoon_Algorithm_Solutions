n, T = map(int, input().split())
w_list = list(map(int, input().split()))
t = 0
for i in range(n):
  t += w_list[i]
  if t > T:
    print(i)
    break
  elif i == n - 1:
    print(n)