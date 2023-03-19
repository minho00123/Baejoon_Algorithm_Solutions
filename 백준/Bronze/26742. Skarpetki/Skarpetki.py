socks = input()
cnt_B = 0
cnt_C = 0
for i in range(len(socks)):
    if socks[i] == 'B':
        cnt_B += 1
    else:
        cnt_C += 1
total_pair = cnt_B // 2 + cnt_C // 2
print(total_pair)
