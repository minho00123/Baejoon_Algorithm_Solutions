S = input()
alphabet_lst = [0] * 26
for i in range(len(S)):
  alphabet_lst[ord(S[i]) - ord('a')] += 1

for i in range(26):
  print(alphabet_lst[i], end=' ')
