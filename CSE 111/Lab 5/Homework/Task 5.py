class Author:
  def __init__(self,name=None):
    self.name=name
    self.dict1={}
    self.count=0
  def addBook(self,bookname,genre):
   if self.name==None:
      print("A book can not be added without author name")
   else:
    self.count+=1
    if genre in self.dict1.keys():
      self.dict1[genre].append(bookname)
    else:
      self.dict1[genre]=[]
      self.dict1[genre].append(bookname)
  def setName(self,name):
    self.name=name
    self.dict1={}
  def printDetail(self):
    print(f"Number of Book(s): {self.count} ")
    print(f"Author Name: {self.name} ")
    for i in self.dict1.keys():
      print(f"{i}: {','.join(self.dict1[i])}")

a1 = Author()
print("=================================")
a1.addBook("Ice", "Science Fiction")
print("=================================")
a1.setName("Anna Kavan")
a1.addBook("Ice", "Science Fiction")
a1.printDetail()
print("=================================")
a2 = Author("Humayun Ahmed")
a2.addBook("Onnobhubon", "Science Fiction")
a2.addBook("Megher Upor Bari", "Horror")
print("=================================")
a2.printDetail()
a2.addBook("Ireena", "Science Fiction")
print("=================================")
a2.printDetail()
print("=================================")
