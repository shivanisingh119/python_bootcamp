'''replace the elements in  a array with average of max and min elents in the array'''
li=list(map(int,input().split()))
avg=0
maxi=li[0]
mini=li[0]
li2=[]
for i in range(len(li)):
    if(li[i]>maxi):
      maxi=li[i]
    if(li[i]<mini):
        mini=li[i]
    avg=(maxi+mini)//2
for i in range(len(li)):
   li[i]=avg
print(li)
