T = int(input())
for _ in range(T):
  H, W, N = map(int, input().split())
  floor = H * 100 if N % H == 0 else N % H * 100
  room = (N // H) if N % H == 0 else N // H + 1
  print(floor + room)