while True:
  try:
    A, B, C = map(int, input().split())
    ans = max(B - A, C - B)
    print(ans - 1)
  except:
    break