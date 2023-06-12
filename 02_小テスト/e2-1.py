# 2-1.py
import random

def bubble_sort(l: list):    
    n = len(l)
    for i in range(n-1):
        for j in range(i+1, n):
            if l[j] > l[i]:
                t = l[j]
                l[j] = l[i]
                l[i] = t

n = 100
l = random.sample(list(range(n)), n)
bubble_sort(l)
print(l)