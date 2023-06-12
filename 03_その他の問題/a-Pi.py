# a 円周率のシュミレーション
import random

N = 10 ** 5

def simulate() -> float:
    cnt = 0

    for _ in [None]*N:
        x = random.random()*2 - 1
        y = random.random()*2 - 1
        
        # check in circle
        if x**2 + y**2 < 1:
            cnt += 1
    
    return cnt / N * 4

n = int(input("n: "))
f = int(input("process: ")) # 0: hidden, 1: show

sum = 0
for i in range(n):
    s = simulate()
    if f == 1: print(f"{i+1}回目: {s}")
    sum += s

print(f"average: {sum/n}")

