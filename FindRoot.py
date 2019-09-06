a=int(input("Enter Value of a:"))
b=int(input("Enter Value of b:"))
c=int(input("Enter Value of c:"))
d=b*b-4*a*c
if d>0:
	print("Root is Irrational")
elif d<0:
	print("Root is Complex Number")
else:
	print("Both Root is Same")