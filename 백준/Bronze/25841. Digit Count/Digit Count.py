n1, n2, o = input().split()
cnt = 0
for i in range(int(n1), int(n2)+1):
  tmp = str(i)
  for j in range(len(tmp)):
    if tmp[j] == o:
      cnt += 1
print(cnt)