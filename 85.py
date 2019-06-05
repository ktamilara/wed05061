a1=input().split()
for i in a1:
	s=set(i)
	if len(s) == len(i):
		print("Yes")
	else:
		print("No")
