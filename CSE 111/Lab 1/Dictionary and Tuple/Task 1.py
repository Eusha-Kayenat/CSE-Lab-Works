inp_1=input("Enter: ").split(",")
inp_2=input("Enter: ").split(",")
dict_1={}
dict_2={}
res={}
for i in inp_1:
  temp=i
  (x,y)=temp.split(":")
  dict_1[x]=int(y)
for j in inp_2:
  temp=j
  (x,y)=temp.split(":")
  dict_2[x]=int(y)
for k in dict_1:
  res[k]=dict_1[k]
for k in dict_1:
  for l in dict_2:
    if k==l:
      res[k]=res[k]+dict_2[l]
    if l in res:
      pass
    else:
      res[l]=dict_2[l]
lst=[]
for val in res.values():
  if val not in lst:
    lst.append(val)
def sort(l) :
  min = l[0]
  for i in range (len(l)-1) :
    if (l[i])<min :
      min = (l[i])
    for j in range (i+1,len(l)) :
      if l[j]< l[i] :
        l[j],l[i]=l[i],l[j]
  return l
val = sort(lst)
tup=tuple(lst)
print(res)
print(f"Values: {tup}")
