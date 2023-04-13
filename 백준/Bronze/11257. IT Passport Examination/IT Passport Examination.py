N = int(input())
for i in range(N):
  cand_num, st, mn, tch = map(int, input().split())
  total_score = st + mn + tch
  result = ""
  if total_score < 55:
    result = "FAIL"
  else:
    if st < 10.5:
      result = "FAIL"
    elif mn < 7.5:
      result = "FAIL"
    elif tch < 12:
      result = "FAIL"
    else:
      result = "PASS"
  print(cand_num, total_score, result)