n=int(input("Number of inputs: "))
lst=[]
for i in range(n):
  inp=(input("Enter your list:")).split()
  lst.append(list(inp))
highest=0
for j in range(len(lst)):
  sum=0
  for k in range(len(lst[j])):
    sum+=int(lst[j][k])
  if sum>highest:
    highest=sum
    index=j
print(highest)
output=[]
for l in lst[index]:
  output.append(int(l))
print(output)
