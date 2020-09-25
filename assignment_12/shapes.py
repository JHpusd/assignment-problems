import matplotlib.pyplot as plt
from math import sqrt


class Rectangle():
    def __init__(self, base, height, color):
        self.base = base
        self.height = height
        self.color = color
        self.perimeter = 2 * self.base + 2 * self.height
        self.area = self.base * self.height
        self.vertices = [
            (0, 0), (0, self.height), (self.base, self.height), (self.base, 0)]

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
        plt.savefig("rectangle.png")

print("Testing class 'Rectangle'...")
rect = Rectangle(5, 2, "red")
rect.describe()
rect.render()
print("\n")


class Triangle():
    def __init__(self, base, height, color):
        self.base = base
        self.height = height
        self.color = color
        self.perimeter = self.base + self.height + sqrt(
            self.base**2 + self.height**2)
        self.area = round((self.base * self.height / 2), 6)
        self.vertices = [(0, 0), (0, self.height), (self.base, 0)]

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
        plt.figure(1)
        plt.gca().set_aspect("equal")
        plt.plot(x, y, color=self.color, linewidth=2.5)
        plt.savefig("triangle.png")

print("Testing class 'Triangle'...")
tri = Triangle(5, 2, "blue")
tri.describe()
tri.render()
