N = int(input())
P = int(input())
discount_lst = [0]

if N >= 5:
  discount_lst.append(500)
if N >= 10:
  discount_lst.append(int(P * 0.1))
if N >= 15:
  discount_lst.append(2000)
if N >= 20:
  discount_lst.append(int(P*0.25))

ans = P - max(discount_lst)
if ans < 0:
  ans = 0
print(ans)