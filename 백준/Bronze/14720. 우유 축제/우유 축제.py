N = int(input())
lst = list(map(int, input().split()))
l = len(lst)
ans = 0
n = -1
i = 0
while lst[i] < l:
  if lst[i] == 0:
    ans += 1
    n = 0
    break
  i += 1

for j in range(i+1, l):
  if n == 0 and lst[j] == 1:
    ans += 1
    n = 1
  elif n == 1 and lst[j] == 2:
    ans += 1
    n = 2
  elif n == 2 and lst[j] == 0:
    ans += 1
    n = 0

print(ans)