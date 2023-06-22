def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        try:
            answer.append(int(my_string[i]))
        
        except:
            continue
    answer.sort()
    return answer