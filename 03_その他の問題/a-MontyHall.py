# モンティ・ホール問題のシュミレーション
import random

def simulate(flag: bool):
    n = [0, 0, 0]
    n[random.randint(0, 2)] = 1 # 正解のドアを指定

    # 最初に 0 番を選んでも一般性を失わない 

    if flag:
        # 変更する場合
        # pick 0 -> show 1 or 2 (c へ変更する)
        c = 1 if n[1] == 1 else 2
        return bool(n[c])

    else: return bool(n[0]) # 変更しない場合


n = int(input("n: "))

print("変更しない場合: ", end="")
cnt = 0
for _ in [None]*n:
    if simulate(False):
        cnt += 1
print(cnt / n)

print("変更した場合  : ", end="")
cnt = 0
for _ in [None]*n:
    if simulate(True):
        cnt += 1
print(cnt / n)
