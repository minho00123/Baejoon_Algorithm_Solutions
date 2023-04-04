import math

N, A, B, C, D = map(int, input().split())
X = math.ceil(N / A) * B
Y = math.ceil(N / C) * D
print(min(X, Y))