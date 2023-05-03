T = int(input())
cnt_A = 0
cnt_B = 0
cnt_C = 0
for i in range(T):
  A, B, C = map(int, input().split())
  cnt_A += A
  cnt_B += B
  cnt_C += C
  if cnt_A < 30 or cnt_B < 30 or cnt_C < 30:
    print('NO')
  else:
    max_p = min(cnt_A, cnt_B, cnt_C)
    print(max_p)
    cnt_A -= max_p
    cnt_B -= max_p
    cnt_C -= max_p
