S = int(input())
M = int(input())
L = int(input())
happy_score = S + (2 * M) + (3 * L)
if happy_score >= 10:
    print('happy')
else:
    print('sad')
