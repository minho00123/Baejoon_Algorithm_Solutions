while True:
  balance, action, cost = input().split()
  if balance == '0' and action == 'W' and cost == '0':
    break
  balance = int(balance)
  cost = int(cost)
  tmp = 0
  if action == 'W':
    tmp = balance - cost
  else:
    tmp = balance + cost
  if tmp < -200:
      print('Not allowed')
  else:
    print(tmp)
