ans_list = []
A, B = map(int, input().split())
C, D = map(int, input().split())
ans_list.append(A/C + B/D)
ans_list.append(C/D + A/B)
ans_list.append(D/B + D/A)
ans_list.append(B/A + D/C)

max_num = max(ans_list)
max_index = -1
for i in range(4):
  if ans_list[i] == max_num:
    max_index = i
    break

print(max_index)
