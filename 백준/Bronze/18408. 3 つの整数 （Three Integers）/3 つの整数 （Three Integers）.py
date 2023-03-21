num_list = list(map(int, input().split()))
cnt_one = 0
cnt_two = 0
for i in range(3):
    if num_list[i] == 1:
        cnt_one += 1
    else:
        cnt_two += 1
if cnt_one > cnt_two:
    print(1)
else:
    print(2)
