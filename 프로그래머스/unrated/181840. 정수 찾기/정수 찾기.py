def solution(num_list, n):
    cnt = 0
    for i in range(len(num_list)):
        if num_list[i] == n:
            cnt += 1
    if cnt == 0:
        return 0
    else:
        return 1