#wap to find the number of rect tiles that can be laid on a rectangular floor

L=eval(input("enter length of floor:"))
B=eval(input("enter breadth of floor:"))
l=eval(input("enter length of tiles:"))
b=eval(input("enter breadth of tiles:"))
number=-(-L*B//l*b)
print("no. of tiles are ",number)