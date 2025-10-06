class Shopidify:
  def __init__(self,name="Guest"):
    self.history={}
    self.transaction={}
    self.count=0
    self.name=name
    if name!="Guest" :
      print(f"Welcome {self.name} to Shopidify")
    else :
      print("Welcome to Shopidify")
  def add_to_cart(self,*args):
    if len(args)==1:
      if type(args[0])==list:
        for i in range(0,len(args[0]),2):
          if args[0][i] in self.history:
            self.history[args[0][i]]+=1
          else:
            self.history[args[0][i]]=args[0][i+1]
      else:
        if args[0] in self.history:
         self.history[args[0]]+=1
        else:
          self.history[args[0]]=1
    else:
       if args[0] in self.history:
        self.history[args[0]]+=1
       else:
          self.history[args[0]]=args[1]

  def display_cart(self):
    print(f"Items in the cart for {self.name}:")
    for k,v in self.history.items():
      print(f"- {k}: {v}x")
  def checkout(self):
    self.count+=1
    self.transaction[self.count]=self.history.copy()
    self.history={}
    print(f"Checkout completed for {self.name}")
  def display_history(self):
    print(f"Purchase history for {self.name}: ")
    for i in self.transaction.keys():
      print(f"Transaction {i}:")
      for k,v in self.transaction[i].items():
           print(f"- {k}: {v}x")

guest_account = Shopidify()
print("1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account = Shopidify("John")
print("2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan", 2)
guest_account.add_to_cart("Luffy Action Figure")
guest_account.display_cart()
print("3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.add_to_cart(["Chocolate Chip Cookies", 3,"Goku Action Figure",2,"Dumbbells-5kg",2])
john_account.display_cart()
print("4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan")
guest_account.display_cart()
print("5xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.checkout()
print("6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.display_history()
print("7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.checkout()
print("8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.display_history()
print("9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
