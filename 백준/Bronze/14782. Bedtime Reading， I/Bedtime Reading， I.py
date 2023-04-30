I = int(input())
s = 0
for i in range(1, I + 1):
  if I % i == 0:
    s += i
print(s)
