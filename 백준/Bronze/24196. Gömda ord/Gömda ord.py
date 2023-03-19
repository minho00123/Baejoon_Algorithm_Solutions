encrypted_str = input()
str_length = len(encrypted_str)
i = 0
while i < str_length:
    print(encrypted_str[i], end='')
    i += (ord(encrypted_str[i]) - 64)
