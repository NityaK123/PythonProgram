x=int(input("Enter number to Check Armstrong or not"))
k=[]
i=0
n=x
while x>0:
	r=x%10
	x=x//10
	j=k.append(r)
	i=i+1
p=0
for l in range(0,i):
	p=p+k[l]**i
if p==n:
	print("Number is Armngstrong:",n,"=",p)
else:
	print("Number is not Armstrong:",n,"!=",p)

