N = int(input())
piece = 1
num = 1
for i in range(N):
  piece += num
  if i % 2 == 0:
    num += 1

print(piece)