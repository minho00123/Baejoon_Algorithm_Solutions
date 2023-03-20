A = int(input())
B = int(input())
total_days = A + (B*7)
if total_days >= 1 and total_days <= 30:
    print(1)
else:
    print(0)
