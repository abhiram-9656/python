#Create a class Rectangle with private attributes length and width. Overload ‘<’  operator to compare the area of 2 rectangles.

class rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def area(self):
            return self.length*self.breadth
    
    def __lt__(self, other):
         return self.area() < other.area()

R1 = rectangle(9, 5)
R2 = rectangle(2, 8) 

if R1 < R2:
     print("rectangle1 has a smaller area.")
else:
     print("rectangle2 has a smaller area.") 

print("area of a rectangle1:", R1.area())
print("area of a rectangle2:", R2.area())

     

