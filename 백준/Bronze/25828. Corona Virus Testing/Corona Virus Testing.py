g, p, t = map(int, input().split())
indi_test = g * p
group_test = p * t + g
if indi_test < group_test:
    print(1)
elif indi_test > group_test:
    print(2)
else:
    print(0)
