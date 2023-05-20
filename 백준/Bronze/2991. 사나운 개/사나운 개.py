A, B, C, D = map(int, input().split())
people_list = list(map(int, input().split()))

for i in people_list:
  cnt = 0
  if 0 < i % (A+B) <= A:
    cnt += 1
  if 0 < i % (C+D) <= C:
    cnt += 1
  print(cnt)
