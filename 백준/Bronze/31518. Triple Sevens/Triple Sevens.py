n = int(input())
ans = 777
for _ in range(3):
    arr = list(map(int, input().split()))
    if 7 not in arr:
      ans = 0
print(ans)
