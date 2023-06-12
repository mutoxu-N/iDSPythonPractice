# a: 一番近い2点

class Point():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @property
    def length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5
    
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Point(self.x - other.x, self.y - other.y)

# クラスのメソッド不使用
# def calc_distance(p: Point, q: Point) -> float:
#     return ((p.x - q.x)**2 + (p.y - q.y)**2) ** 0.5

# クラスのメソッドを使用
def calc_distance(p: Point, q: Point) -> float:
    return (p - q).length

# 点群1
# (0, 0)  (5, 0)  (5, 5)  (0, 5)  (5, 5)
points = (Point(0, 0), Point(5, 0), Point(5, 5), Point(0, 5), Point(5, 5))

# 点群2
# (-5, -5)  (-1, -1)  (1, 1)  (5, 5)
# points = (Point(-5, -5), Point(-1, -1), Point(1, 1), Point(5, 5))

n = len(points)
d, idx = calc_distance(points[0], points[1]), ()

for i in range(n-1):
    for j in range(i+1, n):
        t = calc_distance(points[i], points[j])
        if t <= d:
            d = t
            idx = (i, j)

print("closest pair:", idx)
print("distance:", d)

# 実行結果1
# closest pair: (2, 4)
# distance: 0.0

# 実行結果2
# closest pair: (1, 2)
# distance: 2.8284271247461903
