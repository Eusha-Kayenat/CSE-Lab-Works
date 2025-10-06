class TaxiLagbe:
  def __init__(self,id,area):
    self.id=id
    self.area=area
    self.final=[]
    self.bill=[]
    self.sum=0
    self.count=0
  def addPassenger(self,*args):
    self.count+=len(args)
    if self.count>4:
      print("Taxi Full! No more passengers can be added.")
      return
    else:
      self.names=[]
      for i in args:
        self.names+=(i).split("_")
      for j in range(0,len(self.names),2):
        print(f"Dear {self.names[j]}! Welcome to TaxiLagbe.")
        self.final.append(self.names[j])
      for k in range(1,len(self.names),2):
        self.sum+=int(self.names[k])
  def printDetails(self):
    print(f"Trip info for Taxi number: {self.id}")
    print(f"This taxi can only cover the {self.area} area.")
    print(f"Total passengers: {len(self.final)}")
    pessenger=(",".join(self.final))
    print("Passenger lists:")
    print(pessenger)
    print(f"Total collected fare: {self.sum} Taka")

taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200','Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115', 'Parker_215')
print('-------------------------------')
taxi2.printDetails()
