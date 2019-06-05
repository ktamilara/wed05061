l1=[int(x) for x in input().split()]
for i in range(0,len(l1),2):
	print(abs(l1[i]-l1[i+1]))
