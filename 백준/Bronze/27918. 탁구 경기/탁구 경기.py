N = int(input())
score_D = 0
score_P = 0
for i in range(N):
  winner = input()
  if winner == 'D':
    score_D += 1
  else:
    score_P += 1
  if (score_D - score_P == 2) or (score_P - score_D == 2):
    break

print(f'{score_D}:{score_P}')