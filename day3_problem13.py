# '''find the missing number in an array
# inputs 1 to 10
# 1 2 3 4 6 7 8 9 10
# missing number is 5'''
li=list(map(int,input().split()))
n=int(input())
t=n*(n+1)/2
sum1=0
x=0
for i in range(len(li)):
        sum1+=li[i]
x=t-sum1
print(x)
        
                



    
