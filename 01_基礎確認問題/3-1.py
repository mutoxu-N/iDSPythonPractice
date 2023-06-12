# 3-1

def area(r: int) -> float:
    return 3.14 * (r**2)

r = int(input("r: "))
print(f"半径{r}の円の面積は{area(r)}です。")