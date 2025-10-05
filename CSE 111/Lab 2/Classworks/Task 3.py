def capitalizer(inp):
  new=""
  for i in range(len(inp)+10):
    if i==len(inp):
      break
    else:
      if 65<=ord(inp[0]) and ord(inp[0])<=90:
        new+=inp[0]
      else:
        new+=chr(ord(inp[0])-32)
      if inp[i]=="." or inp[i]=="!" or inp[i]=="?":
          if 65<=ord(inp[i+2]) and ord(inp[i+2])<=90:
            if i==len(inp):
              break
            else:
              new+=inp[i+2]
          else:
            new+=chr(ord(inp[i+2])-32)
      elif inp[i]=="i" and inp[i+1]==" ":
        new+=chr(ord(inp[i])-32)
      else:
        new+=inp[i]
  print(new)
inp=input("Enter your string: ")[2:-2]
print(inp)
capitalizer(inp)
