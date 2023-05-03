p = int(input())
p_name = ['A', 'B', 'C', 'D', 'E', 'F']
p_cards = []
for i in range(p):
  p_cards.append(list(map(int, input().split())))

cards = []
for i in range(p):
  for j in range(1, len(p_cards[i])):
    cards.append(p_cards[i][j])

cards.sort()

for i in range(len(cards)):
  print_index = -1
  for j in range(p):
    try:
      p_cards[j].index(cards[i])
      print_index = j
    except ValueError:
      continue
  print(p_name[print_index], end='')
