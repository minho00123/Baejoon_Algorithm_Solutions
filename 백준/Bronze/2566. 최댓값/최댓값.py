m = [list(map(int, input().split())) for _ in range(9)]

m_num = -1
m_idx1 = 0
m_idx2 = 0

for i in range(9):
  for j in range(9):
    if m[i][j] > m_num:
      m_num = m[i][j]
      m_idx1 = i
      m_idx2 = j

print(m_num)
print(m_idx1 + 1, m_idx2 + 1)
