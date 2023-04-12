people = list(map(int, input().split()))
x, y, r = map(int, input().split())
ans = 0
for i in range(len(people)):
  if x == people[i]:
    ans = i + 1
print(ans)