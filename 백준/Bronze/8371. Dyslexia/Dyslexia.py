n = int(input())
origin_text = input()
pupil_text = input()
cnt = 0
for i in range(n):
  if origin_text[i] != pupil_text[i]:
    cnt += 1
print(cnt)