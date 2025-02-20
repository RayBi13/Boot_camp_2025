import math
class Circle:
    def __init__ (self, radius= None, diameter= None):
        if radius:
            self.radius = radius
        elif diameter:
            self.radius = diameter / 2
        else:
            raise ValueError("Must provide either a radius or a diameter")
    
    def __str__(self):
        # return f"Circle with radius {self.radius}"
        return f"Circle with radius {self.radius}, diameter {self.radius * 2}, area {self.area():.2f}"


# circle = Circle(radius=5)
# print(circle)
    def area(self):
        return math.pi * self.radius ** 2  # formula for the area
# circle1 = Circle(radius=3)
# # print (circle1.area())   
# print(circle1)     
    def __add__(self, other):
        if isinstance(other, Circle):  # "other" is also a Circle
            return Circle(radius=self.radius + other.radius)  
        raise TypeError("You can only add two Circles!")
# circle1= Circle(radius=3)
# circle2= Circle(radius=5)
# circle3= circle1 + circle2
# print(circle3)  # Circle with radius 8
    def __lt__(self, other):
      if isinstance(other, Circle):
        return self.radius < other.radius  
      raise TypeError("You can only compare Circles!")
# circle1= Circle(radius=3)
# circle2= Circle(radius=5)  
# print(circle1 < circle2) # should be True because 3 is smaller than 5
# print(circle2 < circle1)  # False because 5 is bigger than 3  
    def __eq__(self, other):
     if isinstance(other, Circle):
        return self.radius == other.radius  
     raise TypeError("You can only compare Circles!")
# circle1= Circle(radius=3)
# circle2= Circle(radius=5)
# circle3= Circle(radius=3)
# # print(circle1 == circle2)  # sould be False because 3 is not equal to 5
# print(circle1 == circle3)  # should be True because 3 = 3
       
circle1 = Circle(radius=5)
circle2 = Circle(radius=2)
circle3 = Circle(radius=7)

circles = [circle1, circle2, circle3]
sorted_circles = sorted(circles)  # Sorting based on radius (because of __lt__)

for c in sorted_circles:
    print(c)  # this to print circles from smallest to largest radius