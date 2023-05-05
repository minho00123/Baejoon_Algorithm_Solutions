while True:
  n = input()
  if n == '0':
    break
  n_len = len(n)
  total_w = n_len + 1
  for i in range(n_len):
    if n[i] == '0':
      total_w += 4
    elif n[i] == '1':
      total_w += 2
    else:
      total_w += 3
  print(total_w)
