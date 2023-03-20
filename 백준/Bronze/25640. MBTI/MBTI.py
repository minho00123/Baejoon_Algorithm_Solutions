jinho_MBTI = input()
N = int(input())
same_people = 0
for i in range(N):
    friend_MBTI = input()
    if jinho_MBTI == friend_MBTI:
        same_people += 1

print(same_people)
