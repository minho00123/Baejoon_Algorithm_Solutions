zero_nums = list(map(int, input().split()))
people_order = ['A', 'B', 'C']
zero_people = []
one_people = []
for i in range(3):
    if zero_nums[i] == 0:
        zero_people.append(i)
    else:
        one_people.append(i)
if (len(zero_people) == 3) or (len(one_people) == 3):
    print('*')
elif len(zero_people) == 2:
    print(people_order[one_people[0]])
else:
    print(people_order[zero_people[0]])
