class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): #더할 수 있음
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other): #뺄 수 있음
        return Vector2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other): #같은지 비교할 수 있음
        return self.x == other.x and self.y == other.y

    def __str__(self): #print시 호츨 됨
        return '(%g, %g)' %(self.x, self.y)

u = Vector2D(0, 1)
v = Vector2D(1, 0)
w = Vector2D(1, 1)

print(u + v)
print(u - v)
print(u == Vector2D(0, 1))