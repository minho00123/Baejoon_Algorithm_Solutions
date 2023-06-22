def solution(intStrs, k, s, l):
    answer = []
    str_list_l = len(intStrs)
    for i in range(str_list_l):
        n = int(intStrs[i][s:s+l])
        if n > k:
            answer.append(n)
    return answer