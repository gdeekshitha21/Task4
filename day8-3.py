class circle:
    pi=3.141
    def init_(self,radius):
        self.radius=radius

    @classmethod
    def area(cls, radius):
        return cls.pi*radius**2

    @classmethod
    def perimeter(cls, radius):
        return 2*cls.pi*radius
radius=5
area=circle.area(radius)
perimeter=circle.perimeter(radius)

print(f"The area of the circle with radius {radius}is:{area}")
print(f"Thw perimeter of the circle with radius {radius}is: {perimeter}")