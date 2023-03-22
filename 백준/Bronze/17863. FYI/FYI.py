N = input()
flag = 1
for i in range(3):
    if N[i] != '5':
        flag = 0
if flag:
    print('YES')
else:
    print('NO')
