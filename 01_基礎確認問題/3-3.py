import random

class Dice:
    def __init__(self, min, max) -> None:
        self.__min = min
        self.__max = max

    def __str__(self) -> str:
        return f"Dice({self.__min}, {self.__max})"

    def play(self) -> int:
        return random.randint(self.__min, self.__max)
    
d = Dice(1, 6)
print("dice:", d)
print(d.play())