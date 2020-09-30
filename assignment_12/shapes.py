import matplotlib.pyplot as plt
from math import sqrt

# Shapes class is assignment 14

class Shape():
    def __init__(self, base, height, color):
        self.base = base
        self.height = height
        self.color = color
    
    def describe(self):
        print(
            '''Base: {}\nHeight: {}\nColor: {}\nPerimeter: {}\nArea: {}\nVertices: {}'''.format(
            self.base, self.height, self.color,
            self.perimeter, self.area, self.vertices))
    
    def render(self):
        x = []
        y = []
        for pairs in self.vertices:
            x.append(pairs[0])
            y.append(pairs[1])
        x.append(0)
        y.append(0)
        plt.style.use('bmh')
        plt.figure(0)
        plt.gca().set_aspect("equal")
        plt.plot(x, y, color=self.color, linewidth=2.5)
        plt.savefig("shape.png")
        plt.clf()


class Rectangle(Shape):
    def __init__(self, base, height, color):
        super().__init__(base, height, color)
        self.perimeter = 2 * self.base + 2 * self.height
        self.area = self.base * self.height
        self.vertices = [
            (0, 0), (0, self.height), (self.base, self.height), (self.base, 0)]


print("Testing class 'Rectangle'...")
rect = Rectangle(5, 2, "red")
rect.describe()
rect.render()
print("\n")


class Triangle(Shape):
    def __init__(self, base, height, color):
        super().__init__(base, height, color)
        self.perimeter = self.base + self.height + sqrt(
            self.base**2 + self.height**2)
        self.area = round((self.base * self.height / 2), 6)
        self.vertices = [(0, 0), (0, self.height), (self.base, 0)]


print("Testing class 'Triangle'...")
tri = Triangle(5, 2, "blue")
tri.describe()
tri.render()


# 13-1

class Square(Rectangle):
    def __init__(self, base, color):
        # self.base = base
        # height = self.base
        # super().__init__(base, height, color)
        super().__init__(base, base, color)

print("Testing class 'Square'...")
sq = Square(5, 'green')
sq.describe()
sq.render()
