N = int(input())
A_cnt = 0
B_cnt = 0
for _ in range(N):
  A, B = map(int, input().split())
  if A > B:
    A_cnt += 1
  elif A < B:
    B_cnt += 1

print(A_cnt, B_cnt)