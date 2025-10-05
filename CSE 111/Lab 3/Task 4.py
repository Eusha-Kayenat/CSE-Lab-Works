class Student:
  def __init__(self,person,grade,course):
    flag1=True
    flag2=True
    self.name=person
    self.cgpa=grade
    self.courses_taken=course
    if grade<2.00:
      flag1=False
      if 1<=course<=2:
        flag2=True
      else:
        flag2=False
    elif grade>=2.00:
      flag1=True
      if 3<=course<=5:
        flag2=True
      else:
        flag2=False
    if flag1:
      self.student_status="Regular"
    else:
      self.student_status="Probation"
    if flag2:
      self.advising_status="Approved"

    else:
      self.advising_status="Denied"
      self.courses_taken=0
s1 = Student("Clark", 3.45, 4)
print(f"Name: {s1.name}\nCGPA: {s1.cgpa}\nCourses Taken: {s1.courses_taken}")
print(f"Student Status: {s1.student_status}\nAdvising Status: {s1.advising_status}")
print("--------------------------------------------------------------------------------")
s2 = Student("Barry", 1.93, 2)
print(f"Name: {s2.name}")
print(f"Student Status: {s2.student_status}\nAdvising Status: {s2.advising_status}")
print("--------------------------------------------------------------------------------")
s3 = Student("Diana", 2.91, 2)
print(f"Advising Status: {s3.advising_status}\nCourses Taken: {s3.courses_taken}")
print("--------------------------------------------------------------------------------")
s4 = Student("Bruce", 1.52, 5)
print(f"Advising Status: {s4.advising_status}\nCourses Taken: {s4.courses_taken}")
