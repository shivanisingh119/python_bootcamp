'''input:-
 hello-------world
 output:-
 -------hello world
 TESTCASE2:-
 input:- hhello-----wor---ld
 output:------helloworld'''
# print(ord("-"))
inp=input()
count=0
ans=""
for i in inp:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)