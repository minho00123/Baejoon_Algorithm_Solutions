t = int(input())
for _ in range(t):
  n1, n2 = map(int, input().split())
  b_n1 = bin(n1)
  cnt_one = b_n1[2:].count('1')
  if cnt_one % 2 == n2:
    print('Valid')
  else:
    print('Corrupt')