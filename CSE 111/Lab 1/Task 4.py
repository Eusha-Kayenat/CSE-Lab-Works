while True:
  inp=input("Enter: ")
  if inp=="STOP":
    break
  else:
    inp=inp.split()
    N=len(inp)
    check=[]
    for c in range(1,N):
      check.append(c)
    flag=True
    for j in range(N-1):
      dif=abs(int(inp[j+1])-int(inp[j]))
      if dif not in check:
        flag=False
      else:
        continue
    if flag:
      print("UB Jumper")
    else:
      print("Not UB Jumper")
