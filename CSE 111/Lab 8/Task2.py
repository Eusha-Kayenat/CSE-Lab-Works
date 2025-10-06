class  Passenger:
  count=0
  def __init__(self,name,weight=0):
    self.name=name
    self.weight=0
    self.fare=450
    Passenger.count+=1
  def set_bag_weight(self,weight):
    if weight>20:
      if weight>50:
        self.fare+=100
      else:
        self.fare+=50
  def printDetail(self):
    print(f"Name: {self.name}\nBus Fare: {self.fare} Taka")

print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)
