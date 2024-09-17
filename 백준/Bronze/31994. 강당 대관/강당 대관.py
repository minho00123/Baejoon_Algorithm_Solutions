info = []
for _ in range(7):
    name, num = input().split()
    info.append([name, int(num)])
max = -1
max_name = ""
for i in range(7):
    if info[i][1] > max:
        max = info[i][1]
        max_name = info[i][0]
print(max_name)
