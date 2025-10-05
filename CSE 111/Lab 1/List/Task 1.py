lst=[]
lst2=[]
output=[]
while True:
  inp=input("Enter your input: ")
  if inp=="STOP":
    break
  else:
    lst.append(int(inp))
for i in lst:
  if i not in lst2:
    lst2.append(i)
for i in lst2:
  count=0
  for j in lst:
    if i==j:
      count+=1
  print(f"{i}-{count}times")
