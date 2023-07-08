T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  one_leg = (M * 2) - N
  two_leg = M - one_leg
  print(one_leg, two_leg)