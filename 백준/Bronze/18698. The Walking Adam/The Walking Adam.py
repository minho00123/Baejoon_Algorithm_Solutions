T = int(input())
for i in range(T):
  s = input()
  steps = 0
  for j in range(len(s)):
    if s[j] == 'U':
      steps += 1
    else:
      break
  print(steps)
