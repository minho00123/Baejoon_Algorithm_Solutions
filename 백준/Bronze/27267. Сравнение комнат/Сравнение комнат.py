a, b, c, d = map(int, input().split())
M_area = a * b
P_area = c * d
if M_area > P_area:
    print('M')
elif M_area < P_area:
    print('P')
else:
    print('E')
