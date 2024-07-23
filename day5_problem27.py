'''print all the vowels followed by consonants'''

#hello world --> eoohllwrld


abc="bcdfghjklmnpqrstvwxyz"
p=input()
countv=0
countc=0
ans=0
# ans2=0
s=p.lower()
l=["a","e","i","o","u"]
for i in s:
    if i in l:
    #    ans+=i
       print(i,end="")

for i in s:
    if i in abc:
       print(i,end="")
print(i)
