class Rectangle():
    def __init__(self, base, height, color):
        self.base = base
        self.height = height
        self.color = color
        self.perimeter = 2 * self.base + 2 * self.height
        self.area = self.base * self.height
        self.vertices = [(0, 0), (self.base, 0), (0, self.height), (self.base, self.height)]
    
    def describe(self):
        print(
            '''Base: {}\nHeight: {}\nColor: {}\nPerimeter: {}\nArea: {}\nVertices: {}'''.format(
            self.base, self.height, self.color,
            self.perimeter, self.area, self.vertices))

rect = Rectangle(5, 2, "red")
rect.describe()