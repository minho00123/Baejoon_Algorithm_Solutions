n = int(input())
s = input()
coffee_num = 0
cnt = 0
for i in range(n):
  if s[i] == '1':
    coffee_num = 2
    cnt += 1
  else:
    if coffee_num > 0:
      coffee_num -= 1
      cnt += 1
print(cnt)
