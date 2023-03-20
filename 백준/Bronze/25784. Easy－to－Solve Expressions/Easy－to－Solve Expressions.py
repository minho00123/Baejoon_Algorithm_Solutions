num_list = list(map(int, input().split()))
num_list.sort()
if num_list[0] + num_list[1] == num_list[2]:
    print(1)
elif num_list[0] * num_list[1] == num_list[2]:
    print(2)
else:
    print(3)
