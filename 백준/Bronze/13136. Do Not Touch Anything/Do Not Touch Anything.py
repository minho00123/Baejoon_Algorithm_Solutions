R, C, N = map(int, input().split())
min_R = 0
min_C = 0
if R % N != 0:
  min_R = R // N + 1
else:
  min_R = R // N
if C % N != 0:
  min_C = C // N + 1
else:
  min_C = C // N
print(min_R * min_C) 
