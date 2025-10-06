class Spaceship:
  def __init__(self,name,capacity):
    self.name=name
    self.capacity=capacity
    self.currentweight=0
    self.cargo=[]
  def load_cargo(self,metal):
    if self.currentweight+metal.getweight()<=self.capacity:
      self.currentweight+=metal.getweight()
      self.cargo.append(metal.getname())
    else:
      print(f"Warning: Unable to load {metal.getname()} inside {self.name}. Exceeds capacity by {self.currentweight+metal.getweight()-self.capacity}.")
  def display_details(self):
    print(f"Spaceship Name: {self.name}")
    print(f"Capacity: {self.capacity}")
    print(f"Current Cargo Weight: {self.currentweight}")
    print(f"Cargo: {self.cargo}")
class Cargo:
  def __init__(self,name,weight):
    self.__name=name
    self.__weight=weight
  def getname(self):
    return self.__name
  def getweight(self):
    return self.__weight

# Creating spaceships
falcon = Spaceship("Falcon", 50000)
apollo = Spaceship("Apollo", 100000)
enterprise = Spaceship("Enterprise", 220000)
print("1.===================================")
# Creating cargo
gold = Cargo("Gold", 20000)
platinum = Cargo("Platinum", 25000)
dilithium = Cargo("Dilithium", 50000)
trilithium = Cargo("Trilithium", 70000)
neutronium = Cargo("Neutronium", 80000)
print("2.===================================")
# Loading cargo onto spaceships
falcon.load_cargo(gold)
falcon.load_cargo(platinum)
falcon.display_details()
print("3.===================================")
apollo.load_cargo(gold) # Apollo will not reach its total capacity
apollo.display_details()
print("4.===================================")
falcon.load_cargo(neutronium) # This should exceed Falcon's capacity
print("5.===================================")
enterprise.load_cargo(dilithium)
enterprise.load_cargo(trilithium)
enterprise.load_cargo(neutronium) # This should not exceed Enterprise's capacity
enterprise.display_details()
