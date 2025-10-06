class BracuStudent:
  def __init__(self,name,home):
    self.name=name
    self.home=home
    self.buspass=False
  def show_details(self):
    print(f"Student Name: {self.name}")
    print(f"Lives in {self.home}")
    print(f"Have Bus Pass?{self.buspass}")
  def get_pass(self):
    self.buspass=True
class BracuBus:
  def __init__(self,dest,capacity=2):
    self.dest=dest
    self.capacity=capacity
    self.lst=[]
  def show_details(self):
    print(f"Bus Route: {self.dest}")
    print(f"Passengers Count: {len(self.lst)} (Max: {self.capacity})")
    print(f"Passengers On Board: {self.lst}")
  def board(self,*args):
    if len(args)==0:
      print("No passengers!")
    else:
      for i in args:
        if i.buspass==True:
          if i.home==self.dest:
            if len(self.lst)<self.capacity:
              self.lst.append(i.name)
              print(f"{i.name} boarded the bus")
            else:
              print("Bus is full!")
          else:
            print("You got on the wrong bus!")
        else:
          print("You don't have a bus pass!")

st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()
