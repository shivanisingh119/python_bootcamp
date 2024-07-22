import math
from math import sqrt
n=int(input())
if(n>1):
    for i in  range(2,int(sqrt(n))+1):
        if n%i==0:
           print("n is not a prime")
           break
    else:
        print("n is   a prime")
else:
    print("n is not a prime")




a=int(input())
r=a**0.5
count=0
for i in range(2,int(r+1)):
    if a%i==0:
        count=1
        break

