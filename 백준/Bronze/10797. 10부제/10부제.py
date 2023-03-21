day = int(input())
car_list = list(map(int, input().split()))
cnt = 0
for i in range(5):
    if car_list[i] == day:
        cnt += 1
print(cnt)
