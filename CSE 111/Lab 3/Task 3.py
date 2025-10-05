class Contacts:
  def __init__(self,people,num):
    saved={}
    if len(people)!=len(num):
      print("Contacts cannot be saved. Length Mismatch!")
    else:
      for i in range(len(people)):
        saved[people[i]]=num[i]
      print("Contacts saved successfully.")
    self.contactDict=saved
names = ["Emergency", "Father", "Bestie"]
numbers = ["999", "01xx23", "01xx87", "01xx65", "01xx43"]
m1 = Contacts(names, numbers)
print("Saved Contacts:", m1.contactDict)
print("---------------------------------------------")
names.append("Mother")
numbers.pop()
m2 = Contacts(names, numbers)
print("Saved Contacts:", m2.contactDict)
