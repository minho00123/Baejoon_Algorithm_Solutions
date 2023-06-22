def solution(before, after):
    str1 = sorted(before)
    str2 = sorted(after)
    if str1 == str2:
        return 1
    else:
        return 0