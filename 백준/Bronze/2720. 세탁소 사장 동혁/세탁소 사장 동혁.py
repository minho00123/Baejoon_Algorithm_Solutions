N = int(input())
for i in range(N):
  C = int(input())
  Q, D, S, P = 0, 0, 0, 0
  Q = C // 25
  C = C - (Q * 25)
  D = C // 10
  C = C - (D * 10)
  S = C // 5
  C = C - (S * 5)
  P = C // 1
  print(Q, D, S, P)
