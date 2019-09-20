x=65
y=80
l=0
for k in range(1,4):
	for i in range(x,x+k):
		b=chr(i)
		print(b,end="")
	for j in range(y+l,83):
		a=chr(j)
		print(a,end="")
	l=l+1
	print()


"""Pattern is APQR
              ABPQ
              ABCR  """