n = int(input())
q1_cnt = 0
q2_cnt = 0
q3_cnt = 0
q4_cnt = 0
axis_cnt = 0

for _ in range(n):
  x, y = map(int, input().split())
  if x == 0 or y == 0:
    axis_cnt += 1
  elif x > 0 and y > 0:
    q1_cnt += 1
  elif x < 0 and y > 0:
    q2_cnt += 1
  elif x < 0 and y < 0:
    q3_cnt += 1 
  else:
    q4_cnt += 1
    
print(f'Q1: {q1_cnt}')
print(f'Q2: {q2_cnt}')
print(f'Q3: {q3_cnt}')
print(f'Q4: {q4_cnt}')
print(f'AXIS: {axis_cnt}')