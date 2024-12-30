class Circle:
  def __init__(self, radius):
    self.radius = radius

  def calculate_area(self):
    return 3.14 * self.radius ** 2
  def calculate_perimeter(self):
    return 2 * 3.14 * self.radius
  def calculate_diameter(self):
    return 2 * self.radius

circle = Circle(4)

print(f"The area of the circle is : {circle.calculate_area()}")
print(f"The perimeter of the circle is : {circle.calculate_perimeter()}")
print(f"The daimeter of the circle is : {circle.calculate_diameter()}") 