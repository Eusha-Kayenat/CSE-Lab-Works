def amikenomota(height,weight):
  score=round(weight/((height/100)**2),1)
  if score<18.5:
    print(f"Score is {score}.You are Underweight")
  elif 18.5<=score<=24.9:
    print(f"Score is {score}.You are Normal")
  elif 25<=score<=24.9:
    print(f"Score is {score}.You are Overweight")
  elif 30<=score:
    print(f"Score is {score}. You are Obese")
inp=input(('Enter height and weight: '))[1:-1]
(h,w)=tuple((inp).split(","))
h=int(h)
w=int(w)
amikenomota(h,w)
