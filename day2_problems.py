''' print 1 to 100 numbers using for loo
using for loop append 1to 100 num in an empty list
find sum of all the num in a list '''

num=int(input())
for i in range(1,num+1):
    print(i,end=" ")


# num1=int(input())
# list2=[]
# for i in range(1,num+1):
#     list2.append(i)
# print(list2)

num3=list(map(int,input().split()))
sum=0
for i in range(len(num3)):
    sum+=num3[i]
print(sum)

'''6)take a list of elements  '''
