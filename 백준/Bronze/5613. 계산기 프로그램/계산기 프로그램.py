n_list = []
while True:
  n = input()
  if n == '=':
    break
  else:
    n_list.append(n)

ans = int(n_list[0])
for i in range(1, len(n_list), 2):
  if n_list[i] == '+':
    ans += int((n_list[i + 1]))
  elif n_list[i] == '-':
    ans -= int((n_list[i + 1]))
  elif n_list[i] == '*':
    ans *= int((n_list[i + 1]))
  elif n_list[i] == '/':
    ans = ans // int((n_list[i + 1]))
print(ans)