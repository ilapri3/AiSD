import math

class Circle(object):
    def __init__(self, start_x, start_y, radius):
        self.start_x = start_x
        self.start_y = start_y
        self.radius = radius
    
    def length_of_circle(self):
        self.length = 2 * math.pi * self.radius
        return f'Длина окружности: {self.length}'
    
    def square_of_circle(self):
        self.square = math.pi * ((self.radius)**2)
        return f'Площадь окружности: {self.square}'
    
    
circle_1 = Circle(0,0,3)
print(circle_1.length_of_circle())
print(circle_1.square_of_circle())
