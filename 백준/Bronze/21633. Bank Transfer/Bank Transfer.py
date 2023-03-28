k = int(input())
comm = (k * 0.01) + 25
if comm >= 2000:
  print("2000.00")
elif (comm < 2000) and (comm >= 100):
  print(f'{comm:.2f}')
else:
  print("100.00")
