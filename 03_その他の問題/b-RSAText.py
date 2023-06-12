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

def encrypt(message: list[str], key: tuple[int, int]) -> list[str]: # 暗号化
    return [ord(m)**key[0] % key[1] for m in message]

def decrypt(message: int, key: tuple[int, int]) -> int: # 復号化
    return [chr(m**key[0] % key[1]) for m in message]


public, secret = generate_keys(257, 263)

n = input("input: ")
y = encrypt(n, public)
print(f"{n} を暗号化すると -> \"{' '.join(map(str, y))}\"")

x = decrypt(y, secret)
print(f"\"{' '.join(map(str, y))}\" を復号化すると -> {''.join(map(str, x))}")
