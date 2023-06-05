q = int(input())
rules = ['0']
for i in range(q):
  rules.append(input())
r = int(input())
for i in range(r):
  n = int(input())
  if n > q or n < 1:
    print(f'Rule {n}: No such rule')
  else:
    print(f'Rule {n}: {rules[n]}')