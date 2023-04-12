t1, m1, t2, m2 = map(int, input().split())
if (t1 * 60 + m1) > (t2 * 60 + m2):
  t2 += 24
total_t = (t2 * 60 + m2) - (t1 * 60 + m1)
n = total_t // 30
print(total_t, n)
