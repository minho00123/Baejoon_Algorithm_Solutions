A_three = int(input())
A_two = int(input())
A_one = int(input())
B_three = int(input())
B_two = int(input())
B_one = int(input())
A_total = (A_three*3) + (A_two*2) + A_one
B_total = (B_three*3) + (B_two*2) + B_one
if A_total > B_total:
    print('A')
elif A_total < B_total:
    print('B')
else:
    print('T')
