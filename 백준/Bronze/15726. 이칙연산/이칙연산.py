A, B, C = map(int, input().split())
n1 = int(A * B / C)
n2 = int(A / B * C)
print(max(n1, n2))
