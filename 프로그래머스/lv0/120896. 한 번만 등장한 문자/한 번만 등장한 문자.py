def solution(s):
    answer = ''
    alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cnt_list = [0] * 26
    for i in range(len(s)):
        for j in range(26):
            if s[i] == alpha_list[j]:
                cnt_list[j] += 1
    
    for i in range(len(cnt_list)):
        if cnt_list[i] == 1:
            answer += alpha_list[i]
    return answer