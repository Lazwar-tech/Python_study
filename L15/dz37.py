import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_square = self.get_square() + other.get_square()
            new_side = math.sqrt(new_square)
            new_height = new_square/new_side
            return Rectangle(new_side, new_height)
        return None

    def __mul__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            new_square = self.get_square() * n
            new_side = math.sqrt(new_square)
            new_height = new_square / new_side
            return Rectangle(new_side, new_height)
        return None

    def __str__(self):
        return f'Rectangle({self.width}, {self.height})'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
get_r3 = r3.get_square()
print(get_r3)
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'