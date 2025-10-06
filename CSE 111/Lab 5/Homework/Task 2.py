class Foodie:
  def __init__(self,name):
    self.name=name
    self.items={}
    self.bill=0
  def order(self,*args):
    for i in args:
      lst=i.split("-")
      self.items[lst[0]]=int(lst[1])
      self.bill+=int(lst[1])*menu[lst[0]]
      print(f"Ordered - {lst[0]}, quantity - {lst[1]}, price (per Unit) - {menu[lst[0]]}.\nTotal price - {menu[lst[0]]*int(lst[1])}")
  def show_orders(self):
    if len(self.items)==0:
      return(f"{self.name} has 0 item(s) in the cart.\nItems: []\nTotal spent: 0.")
    else:
      out=[]
      for i in self.items.keys():
        out.append(i)
      return(f"{self.name} has {len(self.items)} item(s) in the cart.\nItems: {out}\nTotal spent: {self.bill}")

  def pay_tips(self,tip=None):
    if tip==None:
      print("No tips to the waiter.")
    else:
      self.bill+=tip
      print(f"Gives {tip}/- tips to the waiter.")
menu = {'Chicken Lollipop':15,'Beef Nugget':20,'Americano':180,'Red Velvet':150,'Prawn Tempura':80,'Saute Veg':200}
f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3','Beef Nugget-6','Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6','Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())
