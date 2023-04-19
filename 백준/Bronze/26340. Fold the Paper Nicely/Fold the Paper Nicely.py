n = int(input())
for i in range(n):
  s1, s2, f_num = map(int, input().split())
  print(f'Data set: {s1} {s2} {f_num}')
  for j in range(f_num):
    if s1 > s2:
      s1 = s1 // 2
    else:
      s2 = s2 // 2
  print(max(s1, s2), min(s1, s2))
  print()
