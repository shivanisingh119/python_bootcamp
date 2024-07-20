'''find the sum of squares of a digt in a gven number'''
num=int(input())
sum=0
while(num>0):
    r=num%10
    sum+=r**2
    num=num//10
print(sum)
