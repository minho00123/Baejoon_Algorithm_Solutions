def solution(emergency):
    sorted_list = sorted(emergency, reverse=True)
    answer = []
    for i in range(len(emergency)):
        for j in range(len(sorted_list)):
            if sorted_list[j] == emergency[i]:
                answer.append(j + 1)
    return answer