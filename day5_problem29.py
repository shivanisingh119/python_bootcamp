'''    homework    reverse the string numbers
like 
input:- hello1234world
output:- 4321'''

s=input()
num = ""
reverse = ""
for i in s:
    if i.isdigit():
        num += i
for i in num:
    reverse=i+reverse
print( reverse)

    
