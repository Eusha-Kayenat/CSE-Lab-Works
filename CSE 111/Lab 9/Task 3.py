class SultansDine:
  branches={}
  sold=0
  @classmethod
  def details(cls):
    print(f"Total Number of branch(s): {len(cls.branches)}")
    print(f"Total Sell: {cls.sold} Taka")
    for k,v in cls.branches.items():
      print(f"Branch Name: {k}, Branch Sell: {v} Taka")
      print(f"Branch consists of total sell's: {round((v/cls.sold)*100,2)}%")
  def __init__(self,name):
    self.name=name
    self.sold=0
    SultansDine.branches[self.name]=self.sold
  def sellQuantity(self,number):
    if number<10:
      self.sold+=(number*300)
    elif number<20:
      self.sold+=(number*350)
    else:
      self.sold+=(number*400)
    SultansDine.branches[self.name]=self.sold
    SultansDine.sold+=self.sold
  def branchInformation(self):
    print(f"Branch Name: {self.name}")
    print(f"Branch Sell: {self.sold} Taka")

SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sellQuantity(25)
dhanmondi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()
