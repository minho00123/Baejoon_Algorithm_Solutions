N, M, K = map(int, input().split())
max_num = min(M, K) + min(N-M, N-K)
print(max_num)
