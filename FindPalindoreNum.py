for i in range(1,1000):
	k=0
	j=i
	while i>0:
		r=i%10
		k=k*10+r
		i=i//10
	if k==j:
		print(k)
	