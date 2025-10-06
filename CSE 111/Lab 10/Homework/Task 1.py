class Shape:
  def __init__(self, name='Default', height=0, base=0):
    self.area = 0
    self.name = name
    self.height = height
    self.base = base

  def get_height_base(self):
    return "Height: "+str(self.height)+", Base: "+str(self.base)

#write your code here
class triangle(Shape):
  def calcArea(self):
    self.area = (1/2)*self.base*self.height
  def printDetail(self):
    return f"Shape name: {self.name}\n{super().get_height_base()}\nArea: {self.area}"
class trapezoid(Shape):
  def __init__(self,name,height,base,side):
    super().__init__(name,height,base)
    self.side=side
  def calcArea(self):
    self.area=((self.base+self.side)/2)*self.height
  def printDetail(self):
   return f"Shape name: {self.name}\n{super().get_height_base()}, Side_A: {self.side}\nArea: {self.area}"

tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())
