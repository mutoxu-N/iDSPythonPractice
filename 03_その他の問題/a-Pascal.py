# a: パスカルの三角形
m = int(input("m: ")) # 20

l = [[(1 if i == 0 else 0) for i in range(m)] for _ in [None]*m]

for y in range(1, m):
    for x in range(1, m):
        l[y][x] = l[y-1][x-1] + l[y-1][x]

for y in range(m):
    for x in range(0, y+1):
        print(f"{l[y][x]:5}", end=" ")
    print()