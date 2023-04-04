chars = {
  'a': '4',
  'e': '3',
  'i': '1',
  'o': '0',
  's': '5',
}

s = list(input())
for i in range(len(s)):
  if s[i] in chars:
    s[i] = chars[s[i]]

for i in range(len(s)):
  print(s[i], end='')