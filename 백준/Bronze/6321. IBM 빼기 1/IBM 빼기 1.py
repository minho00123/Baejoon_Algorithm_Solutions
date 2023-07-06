n = int(input())
for i in range(1, n+1):
  s = list(input())
  ans = []
  for j in range(len(s)):
    ans.append(chr((ord(s[j]) - ord('A') + 1) % 26 + ord('A')))
  print(f'String #{i}')
  print(''.join(ans))
  print()