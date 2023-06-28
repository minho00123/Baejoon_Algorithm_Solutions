T = int(input())
for _ in range(T):
  N = int(input())
  credit = 0
  gpa = 0
  for i in range(N):
    C, G = input().split()
    credit += int(C)
    gpa += float(G) * int(C)
  gpa /= credit
  print(f'{credit} {gpa:.1f}')