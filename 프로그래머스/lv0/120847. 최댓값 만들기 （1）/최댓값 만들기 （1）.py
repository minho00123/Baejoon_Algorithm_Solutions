def solution(numbers):
    numbers.sort()
    l = len(numbers)
    return numbers[l-1] * numbers[l-2]