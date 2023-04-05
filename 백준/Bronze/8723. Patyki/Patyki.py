line_lst = sorted(map(int, input().split()))
if line_lst[0] == line_lst[1] == line_lst[2]:
  print(2)
elif line_lst[0]**2 + line_lst[1]**2 == line_lst[2]**2:
  print(1)
else:
  print(0)
