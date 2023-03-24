A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())
lst = [A, B, C, D]
lst.sort()
total = max(E, F)
for i in range(1, 4):
  total += lst[i]
print(total)
