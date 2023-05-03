n, m, k = map(int, input().split())
m_lst = list(map(int, input().split()))
k_lst = list(map(int, input().split()))
a = n - m - k
num_lst = []
for i in range(1, n + 1):
  num_lst.append(i)


for i in range(m):
  for j in range(n):
    if m_lst[i] == num_lst[j]:
      num_lst[j] = ''
for i in range(k):
  for j in range(n):
    if k_lst[i] == num_lst[j]:
      num_lst[j] = ''

print(a)
for i in range(n):
  if num_lst[i] != '':
    print(num_lst[i], end=' ')
