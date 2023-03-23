Bytesia_alphabet = input()
s = 0
for i in range(len(Bytesia_alphabet)):
  s += ord(Bytesia_alphabet[i])
print(chr(2015 - s))
