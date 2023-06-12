# 2-8
import random
random.seed(0)
l = random.sample(range(101), 101) # 0~100 まで数字が入ったランダムなリスト

sum1, sum2 = 0, 0

for i in range(101):
    if i in range(35, 76) and l[i] in range(50, 75): sum1 += l[i]
    elif l[i] == 14 or l[i] == 84: sum2 += i

print(sum1, sum2)


# sum1, sum2 = 0, 0

# for i in range(101):
#     if 35<=i and i<=75 and 50<=l[i] and l[i]<75: sum1 += l[i]
#     elif l[i] == 14 or l[i] == 84: sum2 += i

# print(sum1, sum2)

