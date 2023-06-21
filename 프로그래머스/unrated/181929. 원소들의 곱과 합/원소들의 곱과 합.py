def solution(num_list):
    s = sum(num_list)
    m = 1
    for i in range(len(num_list)):
        m *= num_list[i]
    if m < s**2:
        return 1
    else:
        return 0