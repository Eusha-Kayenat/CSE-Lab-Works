def bill(item,place):
  price=0
  delivery=0
  if item=="BBQ Chicken Cheese Burger":
    price+=250
  elif item=="Beef Burger":
    price+=170
  elif item=="Naga Drums":
    price+=200
  if place=="Mohakhali":
    delivery=40
  else:
    delivery+=60
  tax=(price*8)/100
  price+=tax+delivery
  print(round(price,1))
bill("Beef Burger","Dhanmondi")
