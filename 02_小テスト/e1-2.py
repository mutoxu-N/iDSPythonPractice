# 1-2
# 10000以下の完全数

l = []

for c in range(2, 10001):
    sum = 1
    m = int(c ** 0.5) + 1
    for i in range(2, m):
        if c%i == 0:
            sum += i + c // i

    if sum == c:
        l.append(c)
        
    c += 1

print(f"{len(l)}個")
print(*l)