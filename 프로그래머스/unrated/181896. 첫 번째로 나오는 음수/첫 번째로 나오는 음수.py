def solution(num_list):
    minus_idx = -1
    for i in range(len(num_list)):
        if num_list[i] < 0:
            minus_idx = i
            break
    if minus_idx == -1:
        return -1
    else:
        return minus_idx