# 2-7
a = 3
b = 5
c = a*b

for i in range(101):
    if i%c == 0: continue
    elif i%3 == 0 or i%5 == 0: print(str(i) + " ", end="")

print()