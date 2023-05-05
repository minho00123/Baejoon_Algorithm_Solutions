M = int(input())
cups = [1, 2, 3]
for i in range(M):
  X, Y = map(int, input().split())
  cups[X - 1], cups[Y - 1] = cups[Y - 1], cups[X - 1]

for i in range(3):
  if cups[i] == 1:
    print(i + 1)
