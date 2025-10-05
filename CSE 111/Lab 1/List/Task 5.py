str1=input()
lowc=[]
upc=[]
dig=[]
list1=[]
for i in str1:
  if "a" <= i <= "z":
    lowc.append(i)
  elif "A" <= i <= "Z":
    upc.append(i)
  elif "0" <= i <= "9":
    dig.append(i)
def sorted_list(x):
  n=len(x)
  for i in range(n):
    for j in range(i+1,n):
      if x[i] > x[j]:
        x[i], x[j] = x[j], x[i]
sorted_list(lowc)
sorted_list(upc)
sorted_list(dig)
for i in range(len(dig)):
  for j in range(i + 1, len(dig)):
    if int(dig[i]) % 2 == 0 and int(dig[j]) % 2 != 0:
      dig[i], dig[j] = dig[j], dig[i]
    elif dig[i] > dig[j]:
      dig[i], dig[j] = dig[j], dig[i]
var=""
def final_str(y):
  p=len(y)
  var1=""
  for i in range(p):
    var1+=y[i]
  return var1
var+=final_str(lowc)+final_str(upc)+final_str(dig)
print(var)
