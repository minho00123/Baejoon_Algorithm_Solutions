n, p, h = map(int, input().split())
for _ in range(n):
  price = int(input())
  if price < p:
    print(f'NTV: Dollar dropped by {p - price} Oshloobs')
    p = price
  elif price > p:         
    if price > h:
      print(f'BBTV: Dollar reached {price} Oshloobs, A record!')
      h = price
    p = price