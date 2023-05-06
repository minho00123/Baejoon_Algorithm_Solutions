from sys import stdin

N = int(stdin.readline())
total_tabs = 0
for i in range(N):
  total_tabs += int(stdin.readline())
print(total_tabs + 1 - N)
