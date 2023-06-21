def solution(myString, pat):
    revString = ''
    for i in range(len(myString)):
        if myString[i] == 'A':
            revString += 'B'
        elif myString[i] == 'B':
            revString += 'A'
        else:
            revString += myString[i]
    if revString.find(pat) == -1:
        return 0
    else:
        return 1