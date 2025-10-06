class Farmer:
  def __init__(self,name=None):
    if name==None:
     print("Welcome to your farm!")
    elif type(name)==str:
      self.identity=name
      print(f"Welcome to your farm, {self.identity}!")
    elif type(name)==int:
      self.identity=name
      print(f"Welcome to your farm, {self.identity}!")
    self.crops=[]
    self.fish=[]
  def addCrops(self,*args):
    if len(args)==0:
      print(f"No crop(s) added.")
    else:
      print(f"{len(args)} crop(s) added")
      for i in args:
        self.crops.append(i)
  def addFishes(self,*args):
    if len(args)==0:
      print(f"No fish added.")
    else:
      print(f"{len(args)} fish(s) added")
      for i in args:
        self.fish.append(i)
  def showGoods(self):
    if len(self.crops)==0:
      print(f"You don't have any crop(s).")
    else:
      print(f"You have {len(self.crops)} crop(s):")
      res=(",").join(self.crops)
      print(res)
    if len(self.fish)==0:
      print(f"You don't have any crop(s).")
    else:
      print(f"You have {len(self.fish)} crop(s):")
      res1=(",").join(self.fish)
      print(res1)
f1 = Farmer()
print("-------------------")
f1.addCrops('Rice', "Jute", "Cinnamon")
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")
f2 = Farmer("Korim Mia")
print("-------------------")
f2.addFishes('Pangash', 'Magur')
print("-------------------")
f2.addCrops("Wheat", "Potato")
print("-------------------")
f2.addFishes("Koi", "Tuna", "Sardine")
print("-------------------")
f2.showGoods()
print("-------------------")
f3 = Farmer(2865127000)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")
