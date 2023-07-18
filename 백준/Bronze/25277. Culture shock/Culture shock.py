N = int(input())
s_list = list(input().split())
cnt = 0
for i in range(N):
  if s_list[i] == 'he' or s_list[i] == 'him' or s_list[i] == 'she' or s_list[i] == 'her':
    cnt += 1
print(cnt)