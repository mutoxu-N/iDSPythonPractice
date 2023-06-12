# 1-3
# 素数を100個求める

l = []
n = 2

while len(l) < 100:
    f = True
    m = int(n ** 0.5) + 1

    if n == 2:
        l.append(n)
        n += 1
        continue

    else: 
        for i in range(3, m, 2):
            if n % i == 0:
                f = False
                break

    if f: l.append(n)
    n += 2

print(*l)