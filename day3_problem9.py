''' find the  elements present in (k+n)th index '''
''' sample input 
k is given by user
test case 1:-
k=3
n=2
the input parameters are 3 6 8 4 61 2 
output :- 2
test case 2:-
k=3
n=4
elsements are 80 70 54 36 72
output "error"
 '''

k=int(input())
n=int(input())
l=list(map(int,input().split()))

if(len(l)<(k+n)):
    print("error")
else:
    for i in range(len(l)):
      break
print(l[k+n])
      #break
