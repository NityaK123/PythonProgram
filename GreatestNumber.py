x=int(input("Enter number of Element"))
s=[]
for i in range(0,x):
	k=s.insert(i,int(input()))
print(s)
s.sort()
print("Greatest number is",s[x-1])

	