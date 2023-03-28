T = int(input())
for i in range(T):
  n = int(input())
  for j in range(n):
    A, B = map(int, input().split())
    print(A + B, A * B)
