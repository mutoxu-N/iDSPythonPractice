import random

def selection_sort(l: list):
    for i in range(len(l)):
        m = max(l[i:])
        idx = l.index(m)
        l[idx] = l[i]
        l[i] = m

l = random.sample(list(range(100)), 100)
print("l:", l)
selection_sort(l)
print("sorted:", l)