h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
total_s1 = (h1 * 3600) + (m1 * 60) + s1
total_s2 = (h2 * 3600) + (m2 * 60) + s2
waiting_time = 0
if total_s2 > total_s1:
  waiting_time = total_s2 - total_s1
else:
  waiting_time = total_s2 - total_s1 + 24 * 3600

w_s = waiting_time % 60
w_m = waiting_time // 60 % 60
w_h = waiting_time // 3600

print(f'{w_h:02d}:{w_m:02d}:{w_s:02d}')