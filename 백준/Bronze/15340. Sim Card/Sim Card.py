while True:
  c, d = map(int, input().split())
  if c == 0 and d == 0:
    break;
  else:
    ParsTel = (30 * c) + (40 * d)
    ParsCell = (35 * c) + (30 * d)
    ParsPhone = (40 * c) + (20 * d)
    print(min(ParsTel, ParsCell, ParsPhone))
