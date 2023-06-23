def solution(array):
    answer = 0
    for i in range(len(array)):
        array[i] = str(array[i])
        answer += array[i].count('7')
    return answer