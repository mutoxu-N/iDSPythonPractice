import math

class Rational:
    def __init__(self, numerator: int, denominator: int) -> None:
        """ 
        Args: 
            numerator (int): 分子の値
            denominator (int): 分母の値
        """
        self.__numerator = numerator
        self.__denominator = denominator
        self.__reduction()

    def __str__(self) -> str:
        return str(self.__numerator) if self.__denominator == 1 \
                else f"{self.__numerator}/{self.__denominator}"
    
    
    def __reduction(self) -> None: #約分 (private)
        gcd = math.gcd(self.__numerator, self.__denominator)
        self.__numerator //= gcd
        self.__denominator //= gcd

    def __add__(self, other):
        if isinstance(other, int): 
            return Rational(self.__numerator + self.__denominator*other, 
                            self.__denominator)
        
        elif isinstance(other, self.__class__):
            lcm = math.lcm(self.__denominator, other.__denominator)
            n1, n2 = lcm//self.__denominator, lcm//other.__denominator # 通分用の倍率
            return Rational(self.__numerator*n1 + other.__numerator*n2, lcm)
        
    def __mul__(self, other):
        if isinstance(other, int):
            return Rational(self.__numerator*other, self.__denominator)

        elif isinstance(other, self.__class__):
            return Rational(self.__numerator * other.__numerator,
                            self.__denominator * other.__denominator)
    
    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, self.__class__):
            return self + other * -1
        
    def __truediv__(self, other):
        if isinstance(other, int):
            return self * Rational(1, other)
        
        elif isinstance(other, self.__class__):
            return self * Rational(other.__denominator, other.__numerator)
        
    def __int__(self) -> int:
        return self.__numerator // self.__denominator
    
    def __float__(self) -> float:
        return self.__numerator / self.__denominator


if __name__ == '__main__':
    r1 = Rational(3, 5)
    r2 = Rational(2, 6)
    r3 = Rational(16, 4)
    r4 = Rational(3, 11)
    r5 = Rational(45, 91)
    r6 = Rational(53, 13)
    print("r1:", r1)
    print("r2:", r2)
    print("r3:", r3)
    print("r4:", r4)
    print("r5:", r5)
    print("r6:", r6)\

    print("\nr1 + r2 =", r1 + r2)
    print("r2 + 3 =", r2 + 3)
    print("r2 * r4 =", r2 * r4)
    print("r5 - r4 =", r5 - r4)
    print("r4 / r2 =", r4 / r2)\

    print("\nfloat(r6) =", float(r6))
    print("int(r6) =", int(r6))

# r1: 3/5
# r2: 1/3
# r3: 4
# r4: 3/11
# r5: 45/91
# r6: 53/13
# 
# r1 + r2 = 14/15
# r2 + 3 = 10/3
# r2 * r4 = 1/11
# r5 - r4 = 222/1001
# r4 / r2 = 9/11
#
# float(r6) = 4.076923076923077
# int(r6) = 4