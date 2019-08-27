def fact():
	x=int(input("enter number"))
	for i in range(1,x):
		x=x*i		
	return x
print(fact())