class GreenPhone:
  def __init__(self,x,y,z):
    self.model=x
    self.version=y
    self.cameras=z
  def showSpecification(self):
    print(f"Phone Company: GreenPhone")
    print(f"Model Name: {self.model}")
    print(f"Version Name: {self.version}")
    print(f"Number of Cameras: {self.cameras}")
  def updatePhone(self):
    if self.model=="A1":
      if self.version<14:
        self.version+=1
        print(f"Your phone GreenPhone {self.model} is upgraded to Android version: {self.version}.")
      else:
        print(f"Your phone Greenphone {self.model} is already up to date.")
    elif self.model=="M11":
      if self.version<15:
        self.version+=1
        print(f"Your phone GreenPhone {self.model} is upgraded to Android version: {self.version}.")
      else:
        print(f"Your phone Greenphone {self.model} is already up to date.")
    elif self.model=="U20":
      if self.version<16:
        self.version+=1
        print(f"Your phone GreenPhone {self.model} is upgraded to Android version: {self.version}.")
      else:
        print(f"Your phone Greenphone {self.model} is already up to date.")
print('1=======================')
p1 = GreenPhone('A1', 12, 3)
p2 = GreenPhone('M11', 12, 4)
p3 = GreenPhone('U20', 12, 5)
p1.showSpecification()
print('2=======================')
p2.showSpecification()
print('3=======================')
p1.updatePhone()
print('4=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('5=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('6=======================')
p2.updatePhone()
p3.updatePhone()
print('7=======================')
p1.showSpecification()
p3.showSpecification()
