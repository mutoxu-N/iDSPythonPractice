# 2-6
for y in range(1, 10):
    for x in range(1, 10):
        print(str(x*y).zfill(2)+ " ", end="")
    print()