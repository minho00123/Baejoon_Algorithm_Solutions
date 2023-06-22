def solution(numbers, direction):
    answer = []
    l = len(numbers)
    if direction == 'right':
        answer.append(numbers[l-1])
        for i in range(0, l-1):
            answer.append(numbers[i])
    else:
        for i in range(1, l):
            answer.append(numbers[i])
        answer.append(numbers[0])
    return answer