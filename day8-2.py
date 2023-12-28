class Circle:
    pi=3.141

def init__(self, my_list):
    self.my_list=my_list

def print_list(self):
    print(self.my_list)

def calculate_area(self, radius):
    area= self.pi*radius**2
    return area
circle=Circle([10, 501, 22,37,100,999,87, 351])
circle.print_list()
radius=5
area=circle.calculate_area(radius) 
print(f"The area of the circle with radius{radius}is:{area}")   
