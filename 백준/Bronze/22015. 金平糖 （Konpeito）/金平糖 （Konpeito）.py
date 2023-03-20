num_list = list(map(int, input().split()))
max_num = max(num_list)
additional_num = 0
for i in range(3):
    if num_list[i] < max_num:
        additional_num += max_num - num_list[i]
print(additional_num)
