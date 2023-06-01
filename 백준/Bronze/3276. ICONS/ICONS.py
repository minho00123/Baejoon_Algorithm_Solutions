N = int(input())

row = 0
col = 0

while True:
  if row * col >= N:
    break
  row += 1
  
  if row * col >= N:
    break
  col += 1
print(row, col)