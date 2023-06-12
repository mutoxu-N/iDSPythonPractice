# 2-3
def check(x, st=2) -> str:
    r, m = "", int(x ** 0.5) + 1
    for i in range(st, m):
        if x%i == 0:
            cnt = 0
            while x%i == 0:
                x //= i
                cnt += 1

            return r + (f" x {i}^{cnt}" if cnt > 1 else f" x {i}") + check(x, i)

    return "" if x == 1 else " x " + str(x)

print(16, "=", check(16)[3:])
print(30, "=", check(30)[3:])
print(555, "=", check(555)[3:])
print(2016, "=", check(2016)[3:])
print(31578, "=", check(31578)[3:])
print(2147483648, "=", check(2147483648)[3:])