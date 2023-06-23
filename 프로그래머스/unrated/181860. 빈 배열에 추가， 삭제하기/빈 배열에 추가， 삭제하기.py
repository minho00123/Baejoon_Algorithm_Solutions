def solution(arr, flag):
    answer = []
    l = len(arr)
    for i in range(l):
        if flag[i]:
            for j in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for j in range(arr[i]):
                answer.pop()
    return answer