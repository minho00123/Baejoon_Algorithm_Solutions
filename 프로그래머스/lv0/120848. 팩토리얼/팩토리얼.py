def solution(n):
    fact_list = [0, 1]
    for i in range(2, 11):
        fact_list.append(fact_list[i-1] * i)
    
    answer = 0
    for i in range(len(fact_list)):
        if n >= fact_list[i]:
            answer = i
    return answer