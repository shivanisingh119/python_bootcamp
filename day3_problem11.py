'''find the mximum element in a given list

test case 0:
12 23 36 44 45 57
57


test case 1:-
56 78 -8 12 34 -99
78'''
#li=list(map(int,input().split()))
#print(max(li))


# maxi=li[0]
# for i in range(0,len(li)):
#     if(li[i]>maxi):
#         maxi=li[i]
# print(maxi)

'''' find the minimum element in a given list'''
li=list(map(int,input().split()))
#print(min(li))


maxi=li[0]
for i in range(0,len(li)):
    if(li[i]<maxi):
        maxi=li[i]
print(maxi)
