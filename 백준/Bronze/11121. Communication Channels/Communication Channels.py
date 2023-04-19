T = int(input())
for i in range(T):
  inp, outp = input().split()
  if inp == outp:
    print('OK')
  else:
    print('ERROR')