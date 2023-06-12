# 7-1
# 閏年の判定
n = int(input())

f = False
if n%400 == 0: f = True
elif n%4 == 0 and n%100 != 0: f = True

print("閏年" + ("です。" if f else "ではありません。"))