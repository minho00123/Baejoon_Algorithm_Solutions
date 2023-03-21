Z = int(input())
for i in range(Z):
    W, K = map(int, input().split())
    area = W * K
    print(area // 2)
