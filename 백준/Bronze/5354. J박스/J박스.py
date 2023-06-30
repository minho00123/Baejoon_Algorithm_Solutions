tc = int(input())
for _ in range(tc):
  size = int(input())
  if size < 3:
    for i in range(size):
      print('#' * size)
    print()
  else: 
    print('#' * size)
    for i in range(size - 2):
      print('#' + 'J' * (size - 2) + '#')
    print('#' * size)
    print()