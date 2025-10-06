class Student:
  def __init__(self,name,id,dept="CSE"):
    self.name=name
    self.id=id
    self.dept=dept
    self.sug=""
  def dailyEffort(self,effort):
    self.effort=effort
    if self.effort<=2:
      self.sug="Should give more effort!!"
    elif self.effort<=4:
      self.sug="Keep up the good work!"
    else:
      self.sug="Excellent! Now motivate others."

  def printDetails(self):
    print(f"Name: {self.name}")
    print(f"ID: {self.id}")
    print(f"Department: {self.dept}")
    print(f"Daily Effort: {self.effort} hour(s)")
    print(f"Suggestion: {self.sug}")

harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()
