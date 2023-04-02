# wap to find the type of triangle
a,b,c=[int(i) for i in input("enter the 3 sides").split()]
x=(a!=b and b!=c and c!=a )*"scalene triangle " + (a==b or b==c or c==a)*"isosceles triangle " + (a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2)*" right triangle"
print(x)