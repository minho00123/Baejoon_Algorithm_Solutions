while True:
  H1, M1, H2, M2 = map(int, input().split())
  if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0:
    break;
  total_min1 = H1 * 60 + M1
  total_min2 = H2 * 60 + M2
  if total_min1 > total_min2:
    print(total_min2 + 1440 - total_min1)
  else:
    print(total_min2 - total_min1)
