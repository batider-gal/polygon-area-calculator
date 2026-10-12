class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        get_area = self.width * self.height
        return get_area
    def get_perimeter(self):
        get_perimeter = 2 * (self.width + self.height)
        return get_perimeter
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""

        for i in range(self.height):
            picture += "*" * self.width + "\n"

        return picture
    def get_amount_inside(self, shape):
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height

        return width_fit * height_fit
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)
    def set_width(self, width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.height = height
        self.width = height
    def set_side(self, side):
        self.width = side
        self.height = side
    def __str__(self):
        return f"Square(side={self.width})"
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))


