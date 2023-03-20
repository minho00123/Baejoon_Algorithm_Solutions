meals_available = list(map(int, input().split()))
meals_requested = list(map(int, input().split()))
not_receive_meal = 0
for i in range(3):
    if meals_requested[i] > meals_available[i]:
        not_receive_meal += meals_requested[i] - meals_available[i]

print(not_receive_meal)
