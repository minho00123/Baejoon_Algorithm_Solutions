X, Y = map(int, input().split())
cows = (Y - 2*X) // 2
hens = X - cows
print(hens, cows)
