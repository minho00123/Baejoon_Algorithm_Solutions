N = int(input())
cnt_pt = 0
for i in range(1, N+1):
  for j in range(i+1):
    cnt_pt += i + j
    
print(cnt_pt)
