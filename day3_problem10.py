''' ASKED IN PRODUCT BASED COMPANIES
you are supposed to print the elements in a particular index but the condition is cyclic 
printting
k=3
3 6 8 4 61 2
o/p:- 4

k=8
80 70 54 36 72
o/p= 36'''

k=int(input())
l=list(map(int,input().split()))
#size=len(l)
i=1
for i in range(len(l)):
    if len(l)<k:
        p= k%len(l)
print(l[p])
        
''' '''

        
    
        