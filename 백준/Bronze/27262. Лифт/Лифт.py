n, k, a, b = map(int, input().split())
stair_time = (n - 1) * a
elevator_time = (n + k - 2) * b
print(elevator_time, stair_time)
