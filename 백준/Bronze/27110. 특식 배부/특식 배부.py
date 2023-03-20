N = int(input())
favor_list = list(map(int, input().split()))
max_people = 0
for i in range(3):
    if N <= favor_list[i]:
        max_people += N
    else:
        max_people += favor_list[i]
print(max_people)
