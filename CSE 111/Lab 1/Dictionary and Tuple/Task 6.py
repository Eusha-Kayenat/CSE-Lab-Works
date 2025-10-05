str1=input()
keys=["1","2","3","4","5","6","7","8","9","0"]
symbols=[".,?!","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"," "]
dict1={}
press=""
for i in range(len(keys)):
  if keys[i] not in dict1:
    dict1[keys[i]]=symbols[i]
for i in range(len(str1)):
  a = str1[i]
  if "a"<=a<="z":
    a=chr(ord(a)-32)
  for k,v in dict1.items(): #k=4,v=GHI
    if a in v: #v=GHI a=H
      for j in range(len(v)): #v=GHI j=0,1,2
        if a==v[j]:
          press+=k*(j+1)
print(press)
