h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
s1 += (h1 * 3600) + (m1 * 60)
s2 += (h2 * 3600) + (m2 * 60)
if s1 <= s2:
  print(s2 - s1)
else:
  print((s2 + (3600 * 24)) - s1)
