'''hello123world 
output=6'''

# s=input()
# sum=0
# str="0123456789"

# for i in s:
#     if i in str:
#         sum+=int(i) 
# print(sum)


#sum of digits in a number usi g ASCII
# s=input()
# sum=0

# for i in s:
#      if ord(i)>=48 and ord(i)<=57:
#          sum+=int(i)
# print(sum)

# #COUNT THE  uppercase letters in given string

s=input()
# sum=0

for i in s:
     if ord(i)>=65 and ord(i)<=90:
         
        print(i,end=" ")

#to print  number count of uppercase letter

s=input()
sum=0

for i in s:
     if ord(i)>=65 and ord(i)<=90:
         sum+=1
print(sum)
