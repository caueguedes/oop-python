class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()
p.reset()
print(p.x, p.y)  # 0 0


Point.reset(p)
print(p.x, p.y)  # 0 0 # is the same as before
