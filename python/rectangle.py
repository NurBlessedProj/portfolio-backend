

class Rectangle:
    def __init__(self, length, width) :
        self.length = length
        self.width = width

    def calculate_semi_permeter(self):
        return self.width + self.length
    def calculate_perimeter(self):
        return self.calculate_semi_permeter() * 2
    def calculate_area(self):
       return self.width * self.length

rectangle = Rectangle(10,5)
print(f"Semi Parameter is: {rectangle.calculate_semi_permeter()}")