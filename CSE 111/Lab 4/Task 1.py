class Customer:
  def __init__(self):
    print("Welcome to ABC Memorial Park")
    self.count=0
    self.tp=0
  def buyTicket(self,x,y):
    if self.count<3:
      print(f"Successsfully purchased a ticket for {x}!")
      if y>10:
        self.tp+=100
      else:
        self.tp+=50
      self.count+=1
    else:
      print("You can't buy more than 3 tickets")
  def showDetails(self):
    print(f"Amount of tickets: {self.count}")
    print(f"Total price: {self.tp} Taka")
print('1-------------------------')
customer1=Customer()
print('2-------------------------')
customer1.buyTicket('Bob',23)
customer1.buyTicket('Henry',7)
customer1.buyTicket('Alexa',30)
customer1.buyTicket('Jonas',43)
print('3-------------------------')
customer1.showDetails()
print('4-------------------------')
customer2=Customer()
print('5-------------------------')
customer2.buyTicket('Harry',60)
customer2.buyTicket('Tomas',28)
print('6-------------------------')
customer2.showDetails()
