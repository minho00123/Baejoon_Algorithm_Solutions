def solution(array, n):
    array.sort()
    diff = []
    for i in range(len(array)):
        diff.append(abs(array[i] - n))
    close_num = min(diff)
    print(diff)
    ans_idx = 0
    for i in range(len(diff)):
        if diff[i] == close_num:
            ans_idx = i
            break
    return array[i]