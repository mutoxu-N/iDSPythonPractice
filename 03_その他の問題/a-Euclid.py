# ユークリッドの互除法

def gcd(x: int, y: int) -> int:
    while y != 0:
        t = y
        y = x%t
        x = t
    return x

x, y = map(int, input("x y: ").split())
g = gcd(x, y)
print(f"最大公約数: {g}")
print(f"最小公倍数: {x//g * y}")