while True:
  N, M = map(int, input().split())
  if N == 0 and M == 0:
    break
  else:
    money_lst = list(map(int, input().split()))
    collect_yen = M // N
    total = 0
    for i in range(N):
      if money_lst[i] >= collect_yen:
        total += collect_yen
      else:
        total += money_lst[i]
    print(total)
