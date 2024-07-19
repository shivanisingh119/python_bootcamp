''' 6) take a space separated from a user and print alternate elements  '''
# num=int(input())
# for i in range(0,num+1,2):
#     print(i,end=" ")

l=list(map(int,input().split()))
for i in range(0,len(l),2):
    print(l[i],end=" ")

'''7) you are given with a comma separated natural numbers 1 to 10 print only the even numbers 
 '''