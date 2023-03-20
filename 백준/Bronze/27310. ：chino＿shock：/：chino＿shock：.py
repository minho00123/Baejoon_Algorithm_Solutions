emoji = input()
emoji_length = len(emoji)
underbar_cnt = 0
for i in range(emoji_length):
    if emoji[i] == '_':
        underbar_cnt += 1

input_level = emoji_length + 2 + (underbar_cnt * 5)
print(input_level)
