str1=input()
dict1={}
dict2={}
def new_dict(x,d):
  idx=0
  keys=""
  values=""
  for i in range(len(x)):
    if x[i]==":":
      keys+=x[idx:i-1]
    elif x[i]=="," or i == len(x)-1:
      if i==len(x)-1:
        values+=x[i-5:i+1]
      else:
        values+=x[i-6:i]
      d[keys]=values
      values=""
      keys=""
      idx=i+2
new_dict(str1,dict1)
for key in dict1:
  value = dict1[key]
  if value in dict2:
    dict2[value].append(key)
  else:
    dict2[value]=[key]
print(dict2)
