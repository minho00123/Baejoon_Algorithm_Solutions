def solution(i, j, k):
    answer = 0
    for l in range(i, j+1):
        tmp = str(l)
        for m in range(len(tmp)):
            if tmp[m] == str(k):
                answer += 1  
    return answer