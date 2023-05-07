cnt_people = [0] * 10
total = 0
for i in range(10):
  m, p = map(int, input().split())
  total = total + p - m
  cnt_people[i] = total
print(max(cnt_people))
