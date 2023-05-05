N = int(input())
call_time = list(map(int, input().split()))
cost_Y = 0
cost_M = 0
for i in range(N):
  time_30 = call_time[i] // 30
  time_60 = call_time[i] // 60
  cost_Y += (time_30 + 1) * 10 
  cost_M += (time_60 + 1) * 15

if cost_Y < cost_M:
  print('Y', cost_Y)
elif cost_Y > cost_M:
  print('M', cost_M)
else:
  print('Y', 'M', cost_Y)
