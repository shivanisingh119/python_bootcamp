'''sumof didits
123=1+2+3=6'''
n=int(input())
sum=0
while(n>0):
    r=n%10
    sum+=r     #123%10=3 3%10=3sum+=n
    n=n//10
print(sum)