N = int(input())
cnt = 0
for i in range(1, N+1):
  n = i
  while n != 0:
    if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
      cnt += 1
    n = n // 10
      
print(cnt)