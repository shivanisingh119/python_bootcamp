# #normal print
# print("Hello SWEC")
# print("Sridevi Women's Engineering college")
# #good morning name
# m="madhuri"
# print("good morning",m)
# #taking input fron user
# name=input("enter your name\t")
# print("hello",name)
# #f string =formatted string very very important
# name=input()
# age =int(input())
# print(f"hello {name} you are {age} years old")
#you will take an user name enter marks for each 5 subject from user
#in output statement total 140 average 24 hello srivardhan your marks are 140 and average is 50
name=input()
# sub1=int(input())
# sub2=int(input())
# sub3=int(input())
# sub4=int(input())
# sub5=int(input())
num=int(input())
sub1,sub2,sub3,sub4,sub5=map(int,input().split())
sum=0


sum=sub1+sub2+sub3+sub4+sub5
avg=sum/num
print(f"hello {name}  your total marks are {sum} and average is {avg}")
print(f"hello {name} your total marks is { sub1+sub2+sub3+sub4+sub5 } and average {(sub1+sub2+sub3+sub4+sub5)/num}")
