x=int(input("Enter number to check Palindrome or not:"))
k=0
j=x
while x>0:
	r=x%10
	k=k*10+r
	x=x//10
print(k)
if k==j:
	print("Number is Palindrome")
else:
	print("Number is Not Palindrome")



                                                                      

