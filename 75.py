n1=input()
mid=len(n1)//2
if len(n1)%2!=0:
    for i in range(len(n1)):
        if i==mid:
            print("*",end="")
        else:
            print(n1[i],end="")
else:
    for i in range(len(n1)):
        if i==mid or i==mid-1:
            print("*",end="")
        else:
            print(n1[i],end="")
