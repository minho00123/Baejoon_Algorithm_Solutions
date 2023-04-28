N = int(input())
turn = 0
a = 0
b = 0
while N:
  x = N - (N // 2)
  if turn:
    a += x
  else:
    b += x
  turn ^= 1
  N = N // 2

print(a, b)
