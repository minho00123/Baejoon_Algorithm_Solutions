N = int(input())
cnt = 0
for i in range(N):
  expr_date = input()
  lst = expr_date.split('-')
  if int(lst[1]) <= 90:
    cnt += 1
print(cnt)
