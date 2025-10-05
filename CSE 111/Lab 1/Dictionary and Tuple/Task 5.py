str1=input() 
str2=input() 
dict1={}
dict2={}
def new_dict(x,y):
  for i in x:
    if i in y:
      y[i]+=1
    else:
      y[i]=1
new_dict(str1,dict1)
new_dict(str2,dict2)
flag=None
for i in dict1.keys():
  if i in dict2.keys():
    if dict1[i]==dict2[i]:
      flag=True
    else:
      flag=False
      break
  else:
    flag=False
    break
if flag==True:
  print("Those strings are anagrams")
else:
  print("Those strings are not anagrams")
