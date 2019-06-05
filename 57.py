number1,number2=list(map(int,input().split()))
n=list(map(int,input().split()))
count=0
for i in n:
  if(i==number2):
    count=count+1
print(count)
