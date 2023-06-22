def solution(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    if l1 > l2:
        return 1
    elif l1 < l2:
        return -1
    else:
        s1 = 0
        s2 = 0
        for i in range(l1):
            s1 += arr1[i]
            s2 += arr2[i]
        if s1 > s2:
            return 1
        elif s1 < s2:
            return -1
        else:
            return 0
            