A, P = map(int, input().split())
A_cost = A * 7
P_cost = P * 13
if A_cost > P_cost:
    print('Axel')
elif A_cost < P_cost:
    print('Petra')
else:
    print('lika')
