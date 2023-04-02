a=int(input())
n=a
m=a
i=0
while(m):
    i=i+1
    m=m//10
print(i)
sum=0
for j in range(1,a+1):
    b=a%10
    sum=sum+b**i
    a=a//10
if(sum==n):
    print("yes")
else:
    print("no")