class Library :
  def __init__(self,l,a):
    self.location = l
    self.available = a
    self.borrower = {}
  def details(self):
    print(f"{self.location} Library details")
    print(f"Borrower details:\n{self.borrower}")
    print(f"Books availability:\n{self.available}")

class Reader:
  def __init__(self,x) :
    self.name = x
    self.borrowed = {}
    self.count = 0
  def borrow(self,library,*args) :
    if self.name not in library.borrower.keys() :
      library.borrower[self.name] =0
    for i in args:
        if library.available[i]>0 :
          if self.count<5:
            if i in self.borrowed.keys() :
              self.borrowed[i]+=1
            else :
              self.borrowed[i]=1
            library.available[i]-=1
            print(f"{i} book is borrowed successfully.")
            self.count+=1
            library.borrower[self.name] += 1
          else:
            print("You cannot borrow more than 5 books.")
        else:
          print(f"{i} books are not available at the moment.")
  def readerInfo(self,genre=None) :
    if genre==None :
      print(f"{self.name}, you have {self.count} book(s) with you.")
      for k,v in self.borrowed.items():
        print(f"Books on {k}: {v}")
    else :
      print(f"{self.name}, you have {self.borrowed[genre]} {genre} book(s) with you.")

L1=Library('Dhaka',{'Arts':15,'Fiction':135,'Politics':2,'Science':11,'Poetry':15}) 
L1.details() 
print("1----------------------") 
r1=Reader('Aladdin') 
r1.borrow(L1,'Arts','Fiction','Fiction','Politics') 
print("2----------------------") 
r1.borrow(L1,'Politics','Fiction') 
print("3----------------------") 
r1.readerInfo() 
print("4----------------------") 
r1.readerInfo('Fiction') 
print("5----------------------") 
L1.details() 
print("6----------------------") 
r2=Reader('Jasmine') 
r2.borrow(L1,'Politics','Poetry') 
print("7----------------------") 
r2.readerInfo() 
print("8----------------------") 
L1.details()
