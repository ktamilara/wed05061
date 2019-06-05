import math
a1,b1=map(int,input().split())
c1=(a1*b1)/math.gcd(a1,b1)
print(int(c1))
