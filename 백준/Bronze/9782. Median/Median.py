i = 1
while True:
  n_lst = list(map(int, input().split()))
  if n_lst[0] == 0:
    break
  else:
    median = 0
    n = n_lst[0]
    if n % 2 == 1:
      median = n_lst[((n+1)//2)]
    else:
      median = (n_lst[(n//2)] + n_lst[((n//2)+1)]) / 2
    print(f'Case {i}: {median:0.1f}')
    i += 1
