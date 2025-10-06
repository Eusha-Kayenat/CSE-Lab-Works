class NikeBangladesh:
  branches=[]
  stock={'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
  sold=0
  @classmethod
  def status(cls):
    print("Nike Bangladesh Status:")
    print(f"Branches Opened: {cls.branches}")
    print(f"Currently Stocked\n{cls.stock}")
    print(f"Sold: {cls.sold}")
  def __init__(self,name):
    self.name=name
    self.stock={'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
    NikeBangladesh.branches.append(self.name)
    self.sold=0
  def restockProducts(self,d):
    dic=d
    for i in dic.keys():
      self.stock[i]+=dic[i]
      NikeBangladesh.stock[i]+=dic[i]
  def productSold(self,dic):
    for i in dic.keys():
      self.stock[i]-=dic[i]
      NikeBangladesh.stock[i]-=dic[i]
      self.sold+=dic[i]
      NikeBangladesh.sold+=dic[i]

  def details(self):
    print(f"Nike {self.name} outlet:")
    print(f"Products Currently Stocked:\n{self.stock}")
    print(f"Sold: {self.sold}")

print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts(
{"Air Jordan":1200,"Cortez":200,"Zoom Kobe":200})
chittagong.restockProducts(
{"Air Jordan":1000,"Cortez":250,"Zoom Kobe":100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan":760,"Cortez":90})
chittagong.productSold({"Air Jordan":520,"Zoom Kobe":70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
