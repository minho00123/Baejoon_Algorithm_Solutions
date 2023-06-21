def solution(num_list):
    odd_num = ''
    even_num = ''
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even_num += str(num_list[i])
        else:
            odd_num += str(num_list[i])
    return int(odd_num) + int(even_num)