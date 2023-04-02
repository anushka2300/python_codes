#to calculate amount and simple interest
p=eval(input("enter principal amount"))
r=eval(input("enter rate"))
t=eval(input("enter time"))
SI=(p*r*t)/100
amount=p*(1+r*t)
print("simple interest is",SI)
print("amount  is",amount)