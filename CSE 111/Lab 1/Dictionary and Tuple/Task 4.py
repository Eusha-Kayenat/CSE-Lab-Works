str1=input()+" " 
str2=""
dict1={}
b=0
for i in range(len(str1)):
  if str1[i]==" ":
    str2+=str1[b:i+1]
  else:
    str2+=str1[i]
    b=i+2
for i in str2:
  if i in dict1:
    dict1[i]+=1
  else:
    dict1[i]=1
print(dict1)
