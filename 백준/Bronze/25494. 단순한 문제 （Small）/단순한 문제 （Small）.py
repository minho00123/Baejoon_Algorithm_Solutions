T = int(input())
for i in range(T):
    cnt = 0
    a, b, c = map(int, input().split())
    for j in range(1, a + 1):
        for k in range(1, b + 1):
            for l in range(1, c + 1):
                if ((j % k) == (k % l)) and ((k % l) == (l % j)):
                    cnt += 1
    print(cnt)
