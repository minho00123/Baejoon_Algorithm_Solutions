N = int(input())
S = input()
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_cnt = 0
for i in range(N):
    for j in range(5):
        if S[i] == vowels[j]:
            vowel_cnt += 1
            
print(vowel_cnt)
