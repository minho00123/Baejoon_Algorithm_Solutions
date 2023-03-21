n = int(input())
for i in range(n):
    price = 0
    x = int(input())
    for j in range(x):
        name, quantity, unit = input().split()
        price += int(quantity) * float(unit)
    print(f'${price:.2f}')
