"""classes in python."""

# David Allen

class Rectangle:
    # member variables. do not have to be here
    # self.height etc becomes the member variable - down to preference
    height = 0
    width = 0
    # constructor.
    def __init__(self, height, width):
        self.height = height
        self.width = width
    # calc the area.
    def area(self):
        # area is height x width
        return self.height * self.width
    # calc the perimter    
    def perimeter(self):
        p = (2 * self.height) + self.width
        return p

# create instance.
r1 = Rectangle(10, 35)
# variables can be ammended
r1.height = 20

# another instance
r2 = Rectangle(2, 5)

print("The area of the rectangle is ", r1.area())
print("The area of the other rectangle is ", r2.area())
print("The perimter of the other rectangle is ", r2.perimeter())
# f string - embed expressions inside string
print(f"The area of r1 = {r1.height} x {r1.width} = {r1.area()}")
print(f"The area of r2 = {r2.height} x {r2.width} = {r2.area()}")

# note - alignment is critical!! alignment was out and caused errors
# rectangle not defined etc. 