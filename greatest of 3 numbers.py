#greatest of 3 numbers
a,b,c=[int(i)for i in input("enter the 3 numbers:").split()]
if(a>b):
	if(a>c):
		print("%d is greatest"%a)
	else:
		print("%d is greatest"%c)
elif(a>c):
		if(a>b):
			print("%d is greatest"%a)
		else:
			print("%d is greatest"%b)
		
else:
		print("%d is greatest"%c)		
		