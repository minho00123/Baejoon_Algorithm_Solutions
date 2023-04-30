n = int(input())
m = int(input())
adj = []
nouns = []
for i in range(n):
  adj.append(input())
for i in range(m):
  nouns.append(input())

for i in range(n):
  for j in range(m):
    print(f'{adj[i]} as {nouns[j]}')
