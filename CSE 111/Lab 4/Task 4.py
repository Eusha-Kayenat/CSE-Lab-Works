class StudentDatabase:
  def __init__(self,x,y):
    self.name=x
    self.id=y
    self.grades={}
  def calculateGPA(self,a,b):
    dict1={}
    list1=[]
    for i in range(len(a)):
      list1+=a[i].split(": ")
    list2=[]
    for i in range(0,len(list1),2):
      list2.append(list1[i])
    sub=tuple(list2)
    list3=[]
    for i in range(1,len(list1),2):
      list3.append(list1[i])
    sum=0
    for i in range(len(list3)):
      sum+=float(list3[i])
    cgpa=round(sum/len(list3),2)
    dict1[sub]=cgpa
    self.grades[b]=dict1
  def printDetails(self):
    print(f"Name: {self.name}")
    print(f"ID: {self.id}")
    for k,v in self.grades.items():
      print(f"Courses taken in {k}:")
      for i,j in v.items():
        for k in i:
          print(k)
        print(f"CGPA: {j}")
s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('---------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('---------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('---------------------------------')
s2.printDetails()
