n_list = sorted(list(map(int, input().split())))
print(n_list[0] + n_list[1] + min(n_list[2], n_list[0] + n_list[1] - 1))