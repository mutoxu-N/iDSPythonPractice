# 2-2
class Matrix:

    @property
    def m(self):
        return self.__m
    
    @property
    def n(self):
        return self.__n
    
    @property
    def data(self):
        return self.__data

    def __init__(self, d: list) -> None:
        self.__data = d
        self.__m = len(d)
        self.__n = len(d[0])

    def __str__(self) -> str:
        r = f"Matrix - {self.m}x{self.n}\n"

        for y in self.data:
            r += "  "
            for x in y:
                r += str(x).zfill(2) + " "
            r+= "\n"

        return r[:-1]
    
    def __add__(self, other):
        r = [ [0 for _ in [None]*self.n] for _ in [None]*self.m ]
        for y in range(self.m):
            for x in range(self.n):
                r[y][x] = self.data[y][x] + other.data[y][x]

        return Matrix(r)
    
    def __sub__(self, other):
        r = [ [0 for _ in [None]*self.n] for _ in [None]*self.m ]
        for y in range(self.m):
            for x in range(self.n):
                r[y][x] = self.data[y][x] - other.data[y][x]

        return Matrix(r)
    
    def __mul__(self, other):
        if self.n != other.m: return
        r = [ [0 for _ in [None]*other.n] for _ in [None]*self.m ]
        for y in range(self.m):
            for x in range(other.n):
                for k in range(self.n):
                    r[y][x] += self.data[y][k] * other.data[k][x]

        return Matrix(r)



a = Matrix([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9], 
])
print("A = ")
print(a)

b = Matrix([
    [5, 2, 1], 
    [4, 1, 3], 
    [0, 0, 5], 
])
print("\nB = ")
print(b)

print("\nA x B = ")
print(a * b)