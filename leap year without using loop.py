#wap to find leap year without using loop
a=int(input("enter leap year"))
L=["non leap year","leap year"]
out=L[(a%400==0 or (a%100!=0 and a%4==0))]
print(out)