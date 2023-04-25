x = float(input())
L = 3.785411784
M = 1609.344
ans = L / (x * M * 0.00001)
print(f'{ans:0.6f}')