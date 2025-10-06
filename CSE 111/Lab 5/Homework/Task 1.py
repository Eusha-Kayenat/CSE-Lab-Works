class Student:
  def __init__(self,name,cgpa,cred=9,dept="CSE"):
    self.name=name
    self.cgpa=cgpa
    self.cred=cred
    self.dept=dept
    self.status=""
  def checkScholarshipEligibility(self):
    if self.cgpa>=3.5 and self.cred>10:
      if self.cgpa >=3.7:
        self.status="Merit-based scholarship"
      elif 3.5<=self.cgpa<3.7:
        self.status="Need-based scholarship"
      print(f"{self.name} is eligible for {self.status}.")
    else:
      self.status="No scholarship"
      print(f"{self.name} is not eligible for scholarship.")
  def showDetails(self):
    print(f"Name: {self.name} ")
    print(f"Department: {self.dept}")
    print(f"CGPA: {self.cgpa}")
    print(f"Number of Credits: {self.cred}")
    print(f"Scholarship Status: {self.status}")

print('--------------------------')
std1 = Student("Alif", 3.99, 12)
print('--------------------------')
std1.checkScholarshipEligibility()
print('--------------------------')
std1.showDetails()
print('--------------------------')
std2 = Student("Mim", 3.4)
std3 = Student("Henry", 3.5, 15,"BBA")
print('--------------------------')
std2.checkScholarshipEligibility()
print('--------------------------')
std3.checkScholarshipEligibility()
print('--------------------------')
std2.showDetails()
print('--------------------------')
std3.showDetails()
print('--------------------------')
std4 = Student("Bob", 4.0, 6, "CSE")
print('--------------------------')
std4.checkScholarshipEligibility()
print('--------------------------')
std4.showDetails()
