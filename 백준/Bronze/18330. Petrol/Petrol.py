n = int(input())
k = int(input())
total = min(n, k + 60)
cost = total * 1500 + (n - total)*3000
print(cost)
