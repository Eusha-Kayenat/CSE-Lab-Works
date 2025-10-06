class Student:
  total=0
  brac=0
  other=0
  def __init__(self,name,dept,uni="BRAC University"):
    self.name=name
    self.dept=dept
    self.uni=uni
    Student.total+=1
    if self.uni=="BRAC University":
      Student.brac+=1
    else:
      Student.other+=1
  def individualDetail(self):
    print(f"Name: {self.name}")
    print(f"Department: {self.dept}")
    print(f"Institution: {self.uni}")
  @classmethod
  def printDetails(cls):
    print(f"Total Student(s): {cls.total}")
    print(f"BRAC University Student(s): {cls.brac}")
    print(f"Other Institution Student(s): {cls.other}")
  @classmethod
  def createStudent(cls,name,dept,uni="BRAC University"):
    return cls(name,dept,uni)

Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()
