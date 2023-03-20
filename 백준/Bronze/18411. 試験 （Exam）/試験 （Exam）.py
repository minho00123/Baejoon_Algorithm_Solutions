score_list = list(map(int, input().split()))
score_list.sort()
final_score = score_list[1] + score_list[2]
print(final_score)
