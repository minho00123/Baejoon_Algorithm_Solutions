def solution(myString):
    myString = myString.split('x')
    answer = []
    for i in range(len(myString)):
        answer.append(len(myString[i]))
    return answer