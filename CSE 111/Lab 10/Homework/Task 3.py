class KK_tea :
  sale = {}
  flavour = "Regular"
  def __init__(self,price,bag=50) :
    self.name = f"KK {KK_tea.flavour} Tea"
    if KK_tea.flavour not in KK_tea.sale.keys():
      KK_tea.sale[self.name] = 0
    self.price = price
    self.bag = bag
    self.weight = self.bag*2
    self.status = False
  @classmethod
  def update_sold_status_regular(cls,*args) :
    for i in args :
      cls.sale[i.name]+=1
      i.status = True
  @classmethod
  def total_sales(cls) :
    print(f"Total sales: {cls.sale}")
  def product_detail(self) :
    print(f"Name: KK {self.flavour} Tea, Weight: {self.weight}")
    print(f"Tea Bags: {self.bag}, Price: {self.price}")
    print(f"Status: {self.status}")

class KK_flavoured_tea (KK_tea) :
  def __init__(self,flavour,price,bag) :
    KK_tea.flavour = flavour
    super().__init__(price,bag)
  @classmethod
  def update_sold_status_flavoured(cls,*args) :
    for i in args :
      super().sale[i.name]+=1
      i.status = True

t1 = KK_tea(250)
print("-----------------1-----------------")
t1.product_detail()
print("-----------------2-----------------")
KK_tea.total_sales()
print("-----------------3-----------------")
t2 = KK_tea(470, 100)
t3 = KK_tea(360, 75)
KK_tea.update_sold_status_regular(t1, t2, t3)
print("-----------------4-----------------")
t3.product_detail()
print("-----------------5-----------------")
KK_tea.total_sales()
print("-----------------6-----------------")
t4 = KK_flavoured_tea("Jasmine", 260, 50)
t5 = KK_flavoured_tea("Honey Lemon", 270, 45)
t6 = KK_flavoured_tea("Honey Lemon", 270, 45)
print("-----------------7-----------------")
t4.product_detail()
print("-----------------8-----------------")
t6.product_detail()
print("-----------------9-----------------")
KK_flavoured_tea.update_sold_status_flavoured(t4, t5, t6)
print("-----------------10-----------------")
KK_tea.total_sales()
