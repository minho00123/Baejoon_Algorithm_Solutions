record = input()
score_A = 0
score_B = 0
for i in range(1, len(record)):
  if record[i - 1] == 'A':
    score_A += int(record[i])
  elif record[i - 1] == 'B':
    score_B += int(record[i])

if score_A > score_B:
  print('A')
else:
  print('B')
