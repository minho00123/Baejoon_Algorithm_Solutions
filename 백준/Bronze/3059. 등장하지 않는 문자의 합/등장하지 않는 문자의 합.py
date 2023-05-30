T = int(input())
for i in range(T):
  alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  alpha_sum = 0
  S = list(input())
  for j in range(len(S)):
    for k in range(len(alpha)):
      if S[j] == alpha[k]:
        alpha[k] = ''
  for k in range(len(alpha)):
    if alpha[k] != '':
      alpha_sum += ord(alpha[k])
  print(alpha_sum)
