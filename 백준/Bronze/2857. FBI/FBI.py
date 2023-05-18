fbi_list = []
for i in range(1, 6):
  agent_name = input()
  if agent_name.find('FBI') != -1:
    fbi_list.append(i)
if len(fbi_list) == 0:
  print('HE GOT AWAY!')
else:
  for i in range(len(fbi_list)):
    print(fbi_list[i], end=' ')
