W, N, P = map(int, input().split())
H_i = list(map(int, input().split()))
cnt = 0
for H in H_i:
  if W <= H <= N:
    cnt += 1
print(cnt)