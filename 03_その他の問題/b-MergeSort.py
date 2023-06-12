# b マージソート
import random 

def merge_sort(l: list):
    n = len(l)
    if n == 1: return l
    
    # 分割してマージソート
    listL = l[:n//2]
    listR = l[n//2:]
    merge_sort(listL)
    merge_sort(listR)

    # merge
    i, j, cnt = 0, 0, 0
    while i<len(listL) and j<len(listR):
        if listL[i] < listR[j]:
            l[cnt] = listL[i]
            i += 1
        else: 
            l[cnt] = listR[j]
            j += 1

        cnt += 1

    while i < len(listL):
        l[cnt] = listL[i]
        cnt += 1
        i += 1
    while j < len(listR):
        l[cnt] = listR[j]
        cnt += 1
        j += 1


l = random.sample(range(100), 100)
print("before:", *l)

merge_sort(l)

print("after :", *l)