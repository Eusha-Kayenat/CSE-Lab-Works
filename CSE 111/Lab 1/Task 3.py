lst1=(input("Enter your first list: ")).split()
lst2=(input("Enter your second list: ")).split()
output=[]
for i in range(len(lst1)):
  result=1
  for j in range(len(lst2)):
    result=(int(lst1[i]))*(int(lst2[j]))
    output.append(result)
print(output)
