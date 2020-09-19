class Point:
    def __init__(self, x, y):
        self.move(x, y)

    def move(self, x=0, y=0):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

point1 = Point()
print(point1.x, point1.y)  # 0 0

# Constructing a Point
point2 = Point(3, 5)
print(point2.x, point2.y)  # 3 5
