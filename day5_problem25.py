'''check how many vowels and consonants in the string are there in a given strings'''
#this will include space
# p=input()
# countv=0
# countc=0

# s=p.lower()
# l=["a","e","i","o","u"]
# for i in s:
#     if i in l:
#        countv+=1
#     else:
#        countc+=1
# print(countv,countc)

#this will not include space
#p=input()
abc="bcdfghjklmnpqrstvwxyz"
p=input()
countv=0
countc=0

s=p.lower()
l=["a","e","i","o","u"]
for i in s:
    if i in l:
       countv+=1
for i in s:
    if i in abc:
       countc+=1
print(countv,countc)
