# x の整数乗を効率よく計算

def pow(x: float, n: int) -> float:
    if(n == 1): return x

    v = pow(x, n//2)
    if(n%2 == 0): return v*v
    else: return v*v*x

x = float(input("x: "))
n = int(input("n: "))
print(f"{x} ** {n} = {pow(x, n)}")
