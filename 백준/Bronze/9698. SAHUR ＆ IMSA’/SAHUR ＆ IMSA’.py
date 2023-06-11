T = int(input())
for i in range(1, T+1):
  H, M = map(int, input().split())
  ans_M = H * 60 + M - 45
  if ans_M < 0:
    ans_M += 60 * 24
    print(f'Case #{i}: {ans_M // 60} {ans_M % 60}')
  else:
    print(f'Case #{i}: {ans_M // 60} {ans_M % 60}')
