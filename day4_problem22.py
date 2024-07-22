'''srt the elements first half in ascending order and second half in descending order'''

li=list(map(int,input().split()))
n=len(li)
li.sort()
i=0

while i<n/2:
     print(li[i])
     i=i+1
     j=n-1
     while j>=n/2:
          
         print(li[j],end=" ")
         j=j-1