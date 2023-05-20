score_list = []
for i in range(5):
  a, b, c, d = map(int, input().split())
  score_list.append(a+b+c+d)
winner_num = max(score_list)
winner_idx = -1
for i in range(5):
  if score_list[i] == winner_num:
    winner_idx = i + 1
print(winner_idx, winner_num)
