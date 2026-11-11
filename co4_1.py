# Create Rectangle class with attributes length and breadth and methods to find area and perimeter. Compare two Rectangle objects by their area. 

class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
            return (self.length*self.breadth)
    def perimeter(self):
            return 2*(self.length+self.breadth)
r1=rectangle(10,20)
r2=rectangle(5,15)
print("area of first rectangle=",r1.area())
    
print("area of second the rectangle=",r2.area())  

print("perimeter of first rectangle=",r1.perimeter())

print("perimeter of second rectangle=",r2.perimeter())

if r1.area()<r2.area():
      print("largest",r2.area())
else:
      print("largest",r1.area())