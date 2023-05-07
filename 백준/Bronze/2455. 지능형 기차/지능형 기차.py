cnt_people = [0] * 4
total = 0
for i in range(4):
  m, p = map(int, input().split())
  total = total + p - m
  cnt_people[i] = total
print(max(cnt_people))
