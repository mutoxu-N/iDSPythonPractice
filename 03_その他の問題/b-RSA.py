# RSA 暗号
import math

def generate_keys(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int]]:
    n = p*q
    l = (p-1)*(q-1)

    # calc e: (p-1)(q-1) と互いに素な自然数
    for i in range(2, l):
        if math.gcd(l, i) == 1:
            e = i
            break

    # calc d: e*d を (p-1)(q-1) で割った余り
    for i in range(2, l):
        if e*i % l == 1:
            d = i
            break

    return (e, n), (d, n)

def encrypt(message: int, key: tuple[int, int]) -> int: # 暗号化
    return message**key[0] % key[1]

def decrypt(message: int, key: tuple[int, int]) -> int: # 復号化
    return message**key[0] % key[1]


public, secret = generate_keys(11, 13)

n = int(input("n: "))
y = encrypt(n, public)
print(f"{n:5} を暗号化すると -> {y:5}")

x = decrypt(y, secret)
print(f"{y:5} を復号化すると -> {x:5}")
