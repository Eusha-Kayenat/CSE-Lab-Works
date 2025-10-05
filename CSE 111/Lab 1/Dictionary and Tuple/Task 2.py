dict1={}
while True:
  inp=input()
  if inp=="STOP":
    break
  n=int(inp)
  if n in dict1:
    dict1[n]+=1
  else:
    dict1[n]=1
for k,v in dict1.items():
  print(k,"-",v,"times")
