# 3-2

def is_prime(x: int) -> bool:
    if x < 2: return False # 2未満は素数じゃない
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False # 割り切れたら素数じゃない
    return True

for i in range(2, 100):
    if is_prime(i): print(i, end=" ")