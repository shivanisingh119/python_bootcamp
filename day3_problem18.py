'''rverse a number'''
n=int(input())
rev=0
while(n>0):
    rev=rev*10+n%10  #p=n%10
    n=n//10          #rev=rev*10+p
print(rev)           #n=n//10  
'''the above problem will fail for large numbers 
       it will give  as time exceed error so the solution can be followed '''

'''the below method is very important'''

n=int(input())
rev=""
while(n>0):
    r=n%10    #1234%10==4     123%10==3
    rev=rev+str(r)   #"4"      "3"
    n=n//10      #1234//10==123   
    p=int(rev)
print(type(p))
print(p)
